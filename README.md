UPI Fraud RAG System

This project is a simple Retrieval-Augmented Generation (RAG) system to analyze UPI fraud-related news articles.

It allows you to ask questions and get answers only from the uploaded articles, using a local language model (no paid APIs).

What this project does

Takes UPI-related news articles (PDF / text)

Converts them into searchable text

Finds the most relevant articles for a question

Generates an answer based on those articles only

Tech Used

Python

Sentence Transformers (MiniLM)

FAISS (vector search)

Hugging Face local model (FLAN-T5-Small)

Pandas

upi-fraud-rag/
├── data/
│   ├── raw/          # Raw articles (PDF / text)
│   └── processed/    # Processed text and embeddings
├── src/
│   ├── preprocess.py
│   ├── embed.py
│   ├── save_embeddings.py
│   ├── retriever.py
│   └── rag.py
├── run_pipeline.py   # Runs the full pipeline
├── requirements.txt
├── README.md
└── .gitignore

Output:
Answer generated from the uploaded articles along with source filenames.

<<<<<<< HEAD
Data Note

The articles were collected using web scraping in a separate project.
That scraper is not included here.

Why this project

Works fully offline

No API keys needed

Good example of RAG + local LLM

Useful for learning NLP and LLM systems
=======
# Install dependencies
pip install -r requirements.txt
3. ExecutionTo process the documents and start the QA system:Bashpython run_pipeline.py
Example OutputUser Query: What happens if my UPI-linked number is deactivated?Generated Answer: According to recent reports, if a mobile number is deactivated and reassigned by the telecom provider, the new owner may gain access to the previous user's UPI link, leading to unauthorized fund transfers.Source: Article: "Risk of Reassigned Mobile Numbers in UPI Ecosystem.pdf"Data Source NoteThis repository contains the RAG Engine. The web scraping pipeline used to collect the news articles is maintained in a separate private repository to keep this project focused on NLP and Information Retrieval.Future RoadmapChunking Optimization: Implement Recursive Character Splitting for better context.UI: Build a Streamlit dashboard for easier querying.Reranking: Add a Cross-Encoder stage to improve retrieval precision.Evaluation: Integrate RAGAS scores for faithfulness and relevancy
>>>>>>> ba7429105c1b52d7196a1aec200214eaf64d0ab5
