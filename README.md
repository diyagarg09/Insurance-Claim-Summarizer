# 🛡️ Intelligent Insurance Claim Summarizer
An AI-powered end-to-end pipeline designed to process and summarize massive accident reports (up to 500+ pages) using Large Language Models (LLMs).

## 📊 System Architecture
The project follows a decoupled architecture, separating the file handling, data processing, and AI orchestration layers.



1. **Frontend Layer**: A lightweight JavaScript interface for multi-part file uploads.
2. **API Gateway**: FastAPI (Python) manages asynchronous requests, file storage in `/uploads`, and metadata logging.
3. **Processing Layer**: PyPDF2-based text extraction engine to handle high-volume document parsing.
4. **Persistence Layer**: MongoDB database for indexing claim IDs, processing status, and AI results.
5. **AI Orchestration**: n8n workflow triggers Google Gemini for abstractive summarization of complex legal/medical jargon.

## 🛠️ Tech Stack
- **Frontend**: JavaScript (ES6+), HTML5, CSS3
- **Backend**: Python 3.13, FastAPI, Uvicorn
- **AI/ML**: Google Gemini LLM, Natural Language Processing (NLP)
- **Database**: MongoDB (NoSQL)
- **Automation**: n8n Workflow Engine

## 📂 Project Structure
```text
Accident-Report-AI/
├── backend/                # API & Business Logic
│   ├── main.py             # FastAPI Endpoints
│   ├── database.py         # MongoDB Connection
│   └── processors.py       # PDF Parsing & Text Cleaning
├── frontend/               # UI Implementation
│   ├── index.html          # Dashboard
│   ├── script.js           # API Integration
│   └── style.css           # Aesthetic Styling
├── uploads/                # Temporary File Storage
├── workflow/               # n8n Workflow Exports
└── requirements.txt        # Python Dependencies



                     🔵 ⭕ USER
              |
              v
    🟦 ┌──────────────────────┐
       │   Frontend UI        │
       │ (HTML + JS)          │
       │ Upload PDF           │
       └──────────────────────┘
              |
              v
    🟩 ┌──────────────────────┐
       │ FastAPI Backend      │
       │     (main.py)        │
       └──────────────────────┘
        /        |        \
       v         v         v

🟩 ┌────────────┐ 🟩┌──────────────┐ 🟩 ┌──────────────┐
   │ Save File  │    │ Extract Text │    │ Store Data   │
   │ uploads/   │    │ processors.py│    │ database.py  │
   └────────────┘    └──────────────┘    └──────────────┘
                      |
                      v
            🟣 ☁️ n8n Workflow
                      |
                      v
      🟣 ┌──────────────────────────┐
         │ Google Gemini AI         │
         │ (Summarization Engine)   │
         └──────────────────────────┘
                      |
                      v
        🟣 ┌──────────────────────┐
           │ Summary Generated    │
           └──────────────────────┘
                      |
          ┌───────────┴───────────┐
          v                       v

 🟠┌──────────────────┐     🟦┌────────────────────┐
   │ MongoDB Database │        │ Frontend Display   │
   │ Store Summary    │        │ Show Result        │
   └──────────────────┘        └────────────────────┘



Contribution:

All kinds of contributions are welcome.
Submit a Pull Request
fix a bug
add a new feature
Open an Issue
any suggestions
any questions
 ->>>>consider star this repository :).
