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


<img width="546" height="629" alt="image" src="https://github.com/user-attachments/assets/be203687-b0fb-40fd-9ba2-d606b09d8b76" />


Output:

Answer generated from the uploaded articles along with source filenames.


###Data Note

The articles were collected using web scraping in a separate project.

That scraper is not included here.


###System Architecture

1. **Data Collection**
   - Web scraping of UPI-related news articles
   - Articles saved in PDF format

2. **Preprocessing**
   - PDF text extraction using `pypdf`
   - Text cleaning and filtering
   - Document chunking (300 tokens, 100-token overlap)

3. **Embedding & Indexing**
   - Sentence-transformer embeddings
   - FAISS index for semantic similarity search

4. **Retrieval & RAG**
   - Query embedding
   - Top-k chunk retrieval
   - Mapping chunks back to source PDFs

5. **Evaluation**
   - Weakly supervised queries
   - Retrieval evaluation using Recall@k
   - Filename normalization for robust matching



