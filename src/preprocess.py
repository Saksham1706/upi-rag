import pandas as pd
from pathlib import Path
from pypdf import PdfReader

raw_folder = "data/raw"
output_folder = "data/processed"
output_file = "data/processed/articles.csv"

Path(output_folder).mkdir(exist_ok=True)

data = []

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

        data.append({
            "file_name": pdf.stem,
            "text": article_text
        })

        print(f"Processed: {pdf.name}")

    except Exception as error:
        print(f"Error reading {pdf.name}: {error}")

df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print("\nDone!")
print(f"Total articles saved: {len(df)}")
