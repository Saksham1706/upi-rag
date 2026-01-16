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



<img width="808" height="381" alt="image" src="https://github.com/user-attachments/assets/0ec42c89-2e2d-4211-acf8-d4cf122c5fc3" />

Output:

Answer generated from the uploaded articles along with source filenames.


###Data Note

The articles were collected using web scraping in a separate project.

That scraper is not included here.

Why this project

Works fully offline

No API keys needed

Good example of RAG + local LLM



