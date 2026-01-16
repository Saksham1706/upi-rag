UPI Fraud Analysis: Local RAG SystemAn end-to-end Retrieval-Augmented Generation (RAG) pipeline designed to analyze UPI-related fraud news. This system performs semantic search across PDF documents and generates answers locally, ensuring data privacy and zero API costs.OverviewManually tracking UPI fraud trends across dozens of news reports is inefficient. This project automates the synthesis of information by:Ingesting scraped PDF news articles.Indexing content into a high-performance vector database.Generating concise answers based strictly on retrieved context to minimize hallucinations.System ArchitectureThe pipeline follows a modular design to separate data processing from inference:Extraction: Converts raw PDFs into cleaned, normalized text chunks.Embedding: Uses SentenceTransformers to map text to a 384-dimensional vector space.Indexing: Stores embeddings in a FAISS index for lightning-fast similarity searches.Augmentation: Retrieves the top-k most relevant document snippets.Generation: A local LLM (Hugging Face) synthesizes the final answer using the snippets as a knowledge base.Tech StackComponentTechnologyLanguagePython 3.9+Vector StoreFAISS (Facebook AI Similarity Search)Embeddingssentence-transformers/all-MiniLM-L6-v2LLMLocal Hugging Face Transformers (Quantized)Data HandlingPandas, PyPDFProject StructurePlaintextupi-fraud-rag/
├── data/
│   ├── raw/             # Input PDF articles (User-provided)
│   └── processed/       # FAISS index and metadata
├── src/
│   ├── preprocess.py    # PDF text extraction logic
│   ├── embed.py         # Vectorization & FAISS indexing
│   ├── retriever.py     # Similarity search logic
│   └── rag.py           # LLM Prompting & Answer generation
├── run_pipeline.py      # Master script to execute full flow
└── .gitignore           # Prevents tracking of large data/PDF files
Installation and Usage1. PrerequisitesEnsure you have the PDF articles in data/raw/.2. InstallationBash# Clone the repository
git clone https://github.com/yourusername/upi-fraud-rag.git
cd upi-fraud-rag

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. ExecutionTo process the documents and start the QA system:Bashpython run_pipeline.py
Example OutputUser Query: What happens if my UPI-linked number is deactivated?Generated Answer: According to recent reports, if a mobile number is deactivated and reassigned by the telecom provider, the new owner may gain access to the previous user's UPI link, leading to unauthorized fund transfers.Source: Article: "Risk of Reassigned Mobile Numbers in UPI Ecosystem.pdf"Data Source NoteThis repository contains the RAG Engine. The web scraping pipeline used to collect the news articles is maintained in a separate private repository to keep this project focused on NLP and Information Retrieval.Future RoadmapChunking Optimization: Implement Recursive Character Splitting for better context.UI: Build a Streamlit dashboard for easier querying.Reranking: Add a Cross-Encoder stage to improve retrieval precision.Evaluation: Integrate RAGAS scores for faithfulness and relevancy.