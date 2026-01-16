import pandas as pd
from pathlib import Path
from pypdf import PdfReader

raw_folder = "data/raw"
output_folder = "data/processed"
output_file = "data/processed/articles.csv"

Path(output_folder).mkdir(exist_ok=True)

data = []

def chunk_text(text, chunk_size=300, overlap=100):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


for pdf in Path(raw_folder).glob("*.pdf"):
    try:
        reader = PdfReader(pdf)
        article_text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                article_text += page_text + " "

        article_text = article_text.strip()

        # skip very small or broken files
        if len(article_text) < 500:
            print(f"Skipped (too short): {pdf.name}")
            continue

        # 🔥 CHUNKING LOGIC (NEW)
        chunks = chunk_text(article_text)

        for chunk_id, chunk in enumerate(chunks):
            data.append({
                "file_name": pdf.stem,   # keep stem (no .pdf)
                "chunk_id": chunk_id,
                "text": chunk
            })

        print(f"Processed & chunked: {pdf.name} | Chunks: {len(chunks)}")

    except Exception as error:
        print(f"Error reading {pdf.name}: {error}")

df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print("\nDone!")
print(f"Total chunks saved: {len(df)}")
