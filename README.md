# Research Matching Chatbot

## Team Members

- Shaik Saniya
- Niharika S

Faculty Mentor:
- Rekha Murthy

---

## Project Overview

Research Matching Chatbot is an AI-powered assistant that helps students discover faculty members based on research interests.

The system uses Retrieval-Augmented Generation (RAG) with ChromaDB to perform semantic search over faculty profiles.

---

## Features

- Semantic Faculty Search
- Faculty Profile Retrieval
- Research Trend Discovery
- Collaboration Suggestions
- Human Confirmation before Recommendation
- Interactive Terminal Chatbot

---

## Technologies Used

- Python
- ChromaDB
- Sentence Transformers
- LangChain
- LangGraph
- GitHub

---

## Project Structure

```
research-matching-chatbot
│
├── data/
├── src/
├── chroma_db/
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

```bash
git clone <repository-url>

cd research-matching-chatbot

python -m venv .venv

pip install -r requirements.txt

python src/ingest.py

python main.py
```

---

## Example Queries

- Who works on NLP?
- Tell me about Dr. Anil Kumar
- Show trending research topics
- Find collaboration opportunities in AI

---

## Future Improvements

- Live Tavily API Integration
- LLM-powered recommendations
- Web Interface
- Multi-university Faculty Database
