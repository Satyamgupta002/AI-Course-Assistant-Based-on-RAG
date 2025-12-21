
# 🎓 AI Course Assistant using RAG & LLMs

> **Ask questions. Get precise answers. Jump directly to the exact moment in the video where it’s taught.**

This project is a **full-scale Retrieval-Augmented Generation (RAG) system powered by Large Language Models (LLMs)** that transforms long-form course videos into **queryable, intelligent knowledge**.  
It enables users to ask natural language questions and receive **context-aware answers enriched with exact video timestamps and lecture references**.

This is not a simple chatbot — it is a **production-style AI system** built to handle **hours of video content**, **semantic retrieval**, and **LLM-grounded reasoning**.

---

## 🚀 Why This Project Stands Out

- 🔥 Converts **entire video courses** into searchable AI knowledge  
- 🧠 Uses **LLMs with RAG** to prevent hallucinations  
- ⏱️ Returns **exact timestamps** from source videos  
- 📚 Preserves **context across fragmented transcripts**  
- 💻 Runs **locally using Ollama** (no paid APIs)  
- ⚙️ Designed with scalability and real-world constraints in mind  

---

## 🧠 What the System Does

The system bridges long-form video content and natural language queries by converting videos into searchable **context-aware knowledge**.

Users can:
- Ask questions in plain English  
- Get accurate, grounded answers  
- Instantly know **which video**, **which lecture**, and **which timestamp** explains the concept  

---

## 🏗️ End-to-End System Workflow

### 1️⃣ Video Collection & Normalization
- Downloaded all course videos from an online source.
- Resolved filename conflicts caused by identical names.
- Extracted playlist metadata from CSV.
- Filtered out non-tutorial videos.
- Renamed videos as:  
  **`<tutorial_number> - <lecture_title>`**

### 2️⃣ Audio Extraction
- Extracted audio using **FFmpeg**.
- Audio names derived directly from video filenames for traceability.

### 3️⃣ Speech-to-Text at Scale
- Transcribed audio using **Whisper** with timestamps.
- Distributed processing across multiple **Google Colab** instances.
- Generated structured JSON files with chunks, timestamps, titles, and full transcripts.

### 4️⃣ Context-Preserving Chunking
- Identified context loss due to small chunks.
- Implemented a **chunk-merging strategy** to preserve semantic continuity.

### 5️⃣ Embedding Generation
- Used **Ollama** with **bge-m3** embedding model.
- Generated embeddings for transcript chunks and user queries.
- Stored embeddings and metadata in **Pandas DataFrames**.

### 6️⃣ Intelligent Retrieval
- Applied **cosine similarity (scikit-learn)**.
- Retrieved **Top-K** relevant chunks per query.

### 7️⃣ Persistence
- Stored embeddings using **Joblib** for fast future retrieval.

### 8️⃣ LLM-Powered Answer Generation
- Used **LLaMA 3.2** for reasoning and answer synthesis.
- Passed retrieved chunks and structured prompts.
- Generated answers with precise video references and timestamps.

---

## 🛠️ Tech Stack

- **LLMs**: LLaMA 3.2, Whisper  
- **Embeddings**: bge-m3 (Ollama)  
- **RAG Pipeline**: Cosine similarity, chunk merging  
- **Core Tools**: Python, Pandas, NumPy, Scikit-learn  
- **Media Processing**: FFmpeg  
- **Infrastructure**: Ollama (local), Google Colab  
- **Persistence**: Joblib  

---

## 🎯 Key Capabilities

- Timestamp-level explainability  
- Semantic search over long-form videos  
- Grounded, hallucination-resistant answers  
- Fast inference with persisted embeddings  
- Modular and extensible design  

---

## 📈 Future Enhancements

- Vector databases (FAISS / Chroma)  
- Web-based UI  
- Multi-course support  
- Advanced reranking strategies  

---

## 📖 Why This Matters

This project demonstrates **practical LLM engineering** using RAG to ground answers in real data.  
It solves a real-world problem: **finding exact explanations inside hours of video content**.

---

## 🧠 Final Note

This repository represents a **complete, real-world AI system**, not a demo.  
Every design decision reflects **performance, scalability, and correctness**.
