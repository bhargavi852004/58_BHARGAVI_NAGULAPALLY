# FINWISER.AI — SEC Filing Summarizer & Q&A (RAG)

**Hackathon Track:** F7 – SEC Filing Summarizer & Q&A  
**Team:** 58_BHARGAVI_NAGULAPALLY  
**Repository Type:** Production-style AI system 

---

## 📌 Problem Statement (F7)

**Problem:**  
Query **SEC 10-K / 10-Q filings** and answer **investor-focused questions** with **clear source citations**.

**Dataset:**  
SEC Filings – Kaggle  
https://www.kaggle.com/datasets/kharanshuvalangar/sec-filings

**Expected Outcome:**  
- Index a **small, curated subset** of filings  
- Implement `ask(question)`  
- Return:
  - ✅ Grounded answer  
  - ✅ Source citations (chunk IDs / filing references)  
- Avoid hallucinations (safe refusal if answer not found)

---

## 🎯 Project Vision

**FINWISER.AI** is a **production-grade Retrieval-Augmented Generation (RAG) system** that allows investors to:

1. Select a company and filing type (10-K / 10-Q)
2. Ask financial or risk-related questions
3. Receive **fact-based answers grounded only in SEC filings**
4. View **transparent citations** for every answer

> This project focuses on **accuracy, explainability, and compliance**, not flashy demos.

---

## 🚀 Key Features

- ✅ SEC Filing ingestion & parsing
- ✅ Chunk-level semantic search (RAG)
- ✅ Pinecone vector database
- ✅ FastAPI backend with `/ask` endpoint
- ✅ Citation-backed answers
- ✅ Safe refusal when data is missing
- ✅ Optional Streamlit UI for demo

---

## 🧠 Why This Project Stands Out

| Aspect | Typical Submissions | FINWISER.AI |
|------|---------------------|-------------|
| Dataset Usage | Index everything blindly | Curated, high-quality subset |
| Answers | LLM guesses | Grounded with citations |
| Architecture | Notebook demo | Production-style FastAPI |
| Vector DB | Local-only | Cloud-grade Pinecone |
| Reliability | Hallucinations | Safe refusal enforced |

---

## 🧩 High-Level Architecture
User Question
↓
(Optional) Streamlit UI
↓
FastAPI Backend (/ask)
↓
Embedding Model
↓
Pinecone Vector Search
↓
Relevant Filing Chunks
↓
LLM (Answer Generation)
↓
Answer + Citations


---

## 🛠️ Tech Stack

### Core
- **Python 3.10+**
- **FastAPI** – backend API
- **Pinecone** – vector database
- **Sentence-Transformers** – embeddings (offline-safe)
- **Gemini / LLM API** – answer generation
- **LangChain (conceptual RAG flow)**

### Data & Processing
- `requests`
- `unstructured`
- `pandas`

### Optional UI
- **Streamlit**

---

## 📂 Final Folder Structure
```
58_BHARGAVI_NAGULAPALLY/
│
├── README.md
├── requirements.txt
├── .gitignore
├── run.py
│
├── data/
│   ├── sec_metadata.csv        # Kaggle dataset 
│   └── filings_text/           # Downloaded SEC filings text (generated, ignored)
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_chunking_validation.ipynb
│   └── 03_rag_testing.ipynb
│
├── src/
│   ├── __init__.py
│
│   ├── config/
│   │   ├── settings.py
│   │   └── prompts.py
│
│   ├── ingestion/
│   │   └── fetch_filings.py
│
│   ├── preprocessing/
│   │   └── chunking.py
│
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│
│   ├── agents/
│   │   ├── qa_agent.py
│   │   └── verifier_agent.py
│
│   ├── pipeline/
│   │   └── rag_pipeline.py
│
│   └── api/
│       └── app.py
│
├── streamlit_app/
│   └── app.py
│
├── eval/
│   ├── evaluation_notes.md
│   └── sample_outputs.md
│
└── logs/
    └── app.log

```

---

## 📥 Data Flow Explained

### 1️⃣ Input Data
- **`sec_metadata.csv`**  
  From Kaggle (input file)
- Contains filing URLs, company info, form types

### 2️⃣ Generated Data
- **`filings_text/`**  
  Downloaded SEC filings (output of ingestion step)

> ⚠️ `filings_text/` is **generated**, not manually added.

---

## 🔎 RAG Workflow (Core Logic)

### Indexing Phase
1. Load metadata
2. Select 3–5 companies
3. Download filings
4. Chunk text (500–1000 tokens)
5. Generate embeddings
6. Store vectors in Pinecone

### Question Phase
1. User asks question
2. Embed question
3. Retrieve top-k chunks
4. Generate answer using context only
5. Attach chunk-level citations

---

## 🧪 Example Output

```json
{
  "answer": "Apple reported supply chain disruptions and regulatory risks.",
  "sources": [
    "AAPL_10K_2023_12",
    "AAPL_10K_2023_18"
  ]
}
```


🏁 One-Line Summary

FINWISER.AI is a production-grade RAG system that enables investors to query SEC filings and receive accurate, citation-backed answers through a FastAPI-powered backend.

