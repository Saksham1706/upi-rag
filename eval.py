import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# =========================
# CONFIG
# =========================
EVAL_CSV_PATH = "data/evaluation/eval_questions.csv"
FAISS_INDEX_PATH = "data/processed/faiss.index"
DOC_IDS_PATH = "data/processed/doc_ids.npy"
MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 5

# =========================
# HELPER FUNCTIONS
# =========================
def normalize_filename(name: str) -> str:
    """
    Normalize filenames so that small formatting differences
    (spaces, underscores, case, .pdf) do not break evaluation.
    """
    return (
        str(name)
        .lower()
        .replace(".pdf", "")
        .replace("_", "")
        .replace(" ", "")
        .strip()
    )

# =========================
# LOAD & FIX CSV
# =========================
print("Loading evaluation questions...")
raw_df = pd.read_csv(EVAL_CSV_PATH, header=0)

# Handle malformed CSV saved by Excel (single-column issue)
if len(raw_df.columns) == 1:
    print("⚠️ Detected malformed CSV. Fixing automatically...")
    single_column = raw_df.columns[0]
    eval_df = raw_df[single_column].str.split(",", n=1, expand=True)
    eval_df.columns = ["question", "relevant_file"]
else:
    eval_df = raw_df.copy()
    eval_df.columns = eval_df.columns.str.strip().str.lower()

# Clean text
eval_df["question"] = eval_df["question"].astype(str).str.strip()
eval_df["relevant_file"] = eval_df["relevant_file"].astype(str).str.strip()

print("Detected columns:", eval_df.columns.tolist())
print(f"Total evaluation queries: {len(eval_df)}")

# =========================
# LOAD MODEL & INDEX
# =========================
print("Loading embedding model...")
model = SentenceTransformer(MODEL_NAME)

print("Loading FAISS index...")
index = faiss.read_index(FAISS_INDEX_PATH)

print("Loading document IDs...")
doc_ids = np.load(DOC_IDS_PATH, allow_pickle=True)

# Normalize doc IDs once
normalized_doc_ids = [normalize_filename(f) for f in doc_ids]

# =========================
# EVALUATION
# =========================
hits = 0

for query_number, row in eval_df.iterrows():
    question_text = row["question"]
    ground_truth_file = row["relevant_file"]

    normalized_gt = normalize_filename(ground_truth_file)

    # Embed query
    query_embedding = model.encode([question_text])

    # Search FAISS
    _, retrieved_indices = index.search(query_embedding, TOP_K)

    retrieved_files = [
        doc_ids[doc_index] for doc_index in retrieved_indices[0]
    ]
    normalized_retrieved = [
        normalize_filename(f) for f in retrieved_files
    ]

    # Check hit using normalized filenames
    if normalized_gt in normalized_retrieved:
        hits += 1

    # Debug output (keep for now)
    print(f"\nQuery {query_number + 1}: {question_text}")
    print("Retrieved:", retrieved_files)
    print("Ground Truth:", ground_truth_file)

# =========================
# METRICS
# =========================
recall_at_k = hits / len(eval_df)

print("\n========================")
print(f"Total Queries : {len(eval_df)}")
print(f"Recall@{TOP_K}     : {recall_at_k:.2f}")
print("========================")
