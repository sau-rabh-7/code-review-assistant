from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import CodeInput, CodeReviewReport
from .llm_analyzer import get_llm_review

app = FastAPI(
    title="Code Review Assistant API",
    description="An API that uses an LLM to review source code and provide improvement suggestions.",
    version="1.0.0"
)

# --- CORS Configuration ---
# This allows our React frontend to communicate with the backend.
# The frontend will run on http://localhost:5173 by default with Vite.
origins = [
    "http://localhost:5173",
    "http://localhost:3000", # Common for Create React App
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------------------


@app.post("/review", response_model=CodeReviewReport, summary="Submit Code for Review")
async def create_code_review(code_input: CodeInput):
    if not code_input.code.strip():
        raise HTTPException(status_code=400, detail="Code input cannot be empty.")
    try:
        review_report = get_llm_review(code_input.language, code_input.code)
        return review_report
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred with the LLM service: {str(e)}")


@app.get("/", summary="Root Endpoint")
def read_root():
    return {"message": "Welcome to the Code Review Assistant API. The frontend is likely running on http://localhost:5173"}