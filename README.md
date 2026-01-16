### Local RAG System for UPI News Retrieval

This project implements a **local Retrieval-Augmented Generation (RAG)** pipeline to retrieve and answer questions from **UPI-related news articles**.  
The system processes unstructured PDF news articles, performs semantic retrieval using dense embeddings and FAISS, and evaluates retrieval quality using Recall@k under weakly supervised settings.


### Project Overview

- Collected UPI-related news articles via **web scraping** and stored them as PDFs.
- Extracted and cleaned unstructured text from PDFs.
- Applied **document chunking with overlap** to improve semantic retrieval.
- Generated dense embeddings using **sentence-transformer models** accessed via Hugging Face.
- Indexed embeddings locally using **FAISS** for efficient similarity search.
- Evaluated retrieval quality using **Recall@k**, and iteratively improved performance through chunk-size and overlap tuning.

- Note: The Hugging Face API key is used only to access pretrained models.  
- All preprocessing, embedding generation, indexing, and retrieval run locally.



<img width="546" height="629" alt="image" src="https://github.com/user-attachments/assets/be203687-b0fb-40fd-9ba2-d606b09d8b76" />


Output:
Answer generated from the uploaded articles along with source filenames.


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



