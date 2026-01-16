import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

data_file = "data/processed/articles.csv"
index_file = "data/processed/faiss.index"
id_file = "data/processed/doc_ids.npy"

# load data
df = pd.read_csv(data_file)

texts = df["text"].tolist()
doc_ids = df["file_name"].tolist()

print(f"Total documents: {len(texts)}")

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# create embeddings
print("Creating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

# convert to float32 (required by faiss)
embeddings = np.array(embeddings).astype("float32")

# create faiss index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# save index and ids
os.makedirs("data/processed", exist_ok=True)
faiss.write_index(index, index_file)
np.save(id_file, np.array(doc_ids))

print("FAISS index saved successfully")
