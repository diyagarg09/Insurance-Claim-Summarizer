import os
import httpx
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# .env file se variables load karein
load_dotenv()
print(f"DEBUG: Auth Key is -> {os.getenv('N8N_AUTH_KEY')}")

# Custom modules
try:
    from database import save_to_db
    from processors import extract_text_from_pdf
except ImportError:
    def save_to_db(data): print("Saved to DB:", data)
    def extract_text_from_pdf(path): return "Sample extracted text"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory Setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")

if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Configuration from .env
N8N_URL = os.getenv("N8N_WEBHOOK_URL")
N8N_AUTH_KEY = os.getenv("N8N_AUTH_KEY") # Secret key jo n8n mein set ki hai

@app.get("/")
async def serve_home():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

@app.post("/upload")
async def upload_report(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOADS_DIR, file.filename)
    
    # PDF Save
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Text Extraction
    text = extract_text_from_pdf(file_path)

    # Authentication Headers
    headers = {
        "X-API-KEY": N8N_AUTH_KEY  # n8n Webhook Header Auth ke liye
    }

    async with httpx.AsyncClient() as client:
        try:
            payload = {"text": text[:5000]} 
            # Headers pass karna zaroori hai
            response = await client.post(N8N_URL, json=payload, headers=headers, timeout=120.0) 
            
            summary_data = response.json()
            print(f"DEBUG: n8n returned: {summary_data}") 

            if isinstance(summary_data, list) and len(summary_data) > 0:
                summary = summary_data[0].get("summary")
                if not summary:
                    summary = f"Key mismatch! n8n sent: {summary_data[0]}"
            elif isinstance(summary_data, dict):
                summary = summary_data.get("summary", f"Key mismatch! Got: {summary_data}")
            else:
                summary = "n8n returned empty or unexpected format."

        except Exception as e:
            print(f"Connection Error: {e}")
            summary = f"Connection error: {str(e)}"

    # Save to MongoDB
    save_to_db({"filename": file.filename, "summary": summary, "status": "Done"})

    return {"summary": summary}