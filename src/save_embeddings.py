import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer

DATA_PATH = "data/processed/articles.csv"
SAVE_PATH = "data/processed/embeddings.pkl"

print("Loading articles...")
df = pd.read_csv(DATA_PATH)
texts = df["text"].tolist()

print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Creating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

print("Saving embeddings...")
with open(SAVE_PATH, "wb") as f:
    pickle.dump(embeddings, f)

print("✅ embeddings.pkl created successfully")
