UPI Fraud RAG Project
What is this project?

This project builds a question-answering system over UPI-related news articles using a Retrieval-Augmented Generation (RAG) approach.

Instead of searching articles manually, you can ask a question and get:

a short answer

based only on relevant articles

with source references

The system works completely locally without paid APIs.

What problem does it solve?

News articles about UPI often contain important information about:

fraud cases

user mistakes

operational risks

Reading many articles manually is slow.
This project helps extract answers automatically from multiple articles.

How it works (simple flow)
PDF Articles
   ↓
Text extraction
   ↓
Vector embeddings
   ↓
FAISS similarity search
   ↓
Local language model
   ↓
Final answer + sources

Folder structure
llm-articles/
│
├── data/
│   ├── raw/            # PDF articles
│   └── processed/      # CSV, embeddings, FAISS index
│
├── src/
│   ├── preprocess.py
│   ├── embed.py
│   ├── save_embeddings.py
│   └── rag.py
│
├── run_pipeline.py     # Runs all steps together
└── README.md

How to run the project
1️⃣ Activate virtual environment
venv\Scripts\activate

2️⃣ Run the full pipeline
python run_pipeline.py


This will:

process PDFs

create embeddings

build FAISS index

run the RAG system

Example question

Question

What are common UPI fraud issues mentioned in recent articles?


Answer

A common issue occurs when a UPI-linked mobile number is deactivated and reassigned,
causing money to be transferred to the wrong person.


Source

Transferred money to wrong UPI linked mobile number

Tools and libraries used

Python

Pandas

SentenceTransformers

FAISS

Hugging Face Transformers

PyPDF

Why a small local model?

Works on laptops with limited RAM

No API keys needed

Fully offline

Stable and reproducible

The model focuses on retrieved context, not general knowledge.

What I learned from this project

Building an end-to-end RAG pipeline

Working with unstructured PDF data

Using vector databases for semantic search

Handling context length limitations

Making practical engineering trade-offs