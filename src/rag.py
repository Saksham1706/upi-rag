import os
import faiss
import pickle
import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


# ----------------------------
# PATHS
# ----------------------------
DATA_PATH = "data/processed/articles.csv"
FAISS_INDEX_PATH = "data/processed/faiss.index"
EMBEDDINGS_PATH = "data/processed/embeddings.pkl"

EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_NAME = "google/flan-t5-small"


# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv(DATA_PATH)
texts = df["text"].tolist()
file_names = df["file_name"].tolist()

# Load embeddings + FAISS
with open(EMBEDDINGS_PATH, "rb") as f:
    embeddings = pickle.load(f)

index = faiss.read_index(FAISS_INDEX_PATH)

# Load embedding model
embedder = SentenceTransformer(EMBED_MODEL_NAME)

# Load local LLM
print("Loading local LLM (flan-t5-small)...")
tokenizer = AutoTokenizer.from_pretrained(LLM_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(LLM_NAME)

llm = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU
)


# ----------------------------
# FRAUD SENTENCE FILTER
# ----------------------------
def extract_fraud_sentences(text):
    keywords = [
        "fraud", "wrong", "mistake", "scam",
        "unauthorized", "cheated", "incorrect",
        "transferred", "lost money"
    ]

    sentences = text.split(".")
    selected = []

    for s in sentences:
        if any(k in s.lower() for k in keywords):
            selected.append(s.strip())

    return ". ".join(selected[:6])  # keep context short


# ----------------------------
# RETRIEVE CONTEXT
# ----------------------------
def retrieve_context(query, top_k=5):
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), top_k)

    filtered_chunks = []
    sources = []

    for idx in I[0]:
        raw_text = texts[idx]
        filtered_text = extract_fraud_sentences(raw_text)

        if filtered_text:
            filtered_chunks.append(filtered_text)
            sources.append(file_names[idx])

    context = "\n".join(filtered_chunks)
    return context, list(set(sources))


# ----------------------------
# ASK LLM
# ----------------------------
def ask_llm(question):
    context, sources = retrieve_context(question)

    if not context.strip():
        return "No relevant context found.", sources

    prompt = (
        "Based on the context below, list common UPI fraud or mistake cases.\n"
        "Answer in short bullet points.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}\n\n"
        "Answer:"
    )

    try:
        response = llm(
            prompt,
            max_new_tokens=120,
            do_sample=False
        )
        answer = response[0]["generated_text"]
    except Exception as e:
        answer = f"LLM error: {e}"

    return answer, sources


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    question = "What are common UPI fraud issues mentioned in recent articles?"

    answer, sources = ask_llm(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for s in sources:
        print("-", s)
