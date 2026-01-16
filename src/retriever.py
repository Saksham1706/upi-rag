import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# paths
index_path = "data/processed/faiss.index"
id_path = "data/processed/doc_ids.npy"
data_path = "data/processed/articles.csv"

# load data
index = faiss.read_index(index_path)
doc_ids = np.load(id_path)
df = pd.read_csv(data_path)

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def search_articles(query, top_k=5):
    query_vector = model.encode([query])
    query_vector = np.array(query_vector).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "file_name": doc_ids[idx],
            "score": distances[0][i],
            "text": df.iloc[idx]["text"][:500]  # preview
        })

    return results

# test search
if __name__ == "__main__":
    user_query = "UPI fraud and security issues"
    results = search_articles(user_query)

    print(f"\nQuery: {user_query}\n")
    for r in results:
        print("File:", r["file_name"])
        print("Score:", r["score"])
        print("Preview:", r["text"])
        print("-" * 40)
