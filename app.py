from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import analyze_requirement
from fastapi.responses import StreamingResponse

app = FastAPI(
    title="Engineering Intelligence Agent",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequirementRequest(BaseModel):
    ticket: str

@app.post("/analyze")
def analyze(request: RequirementRequest):
    result = analyze_requirement(request.ticket)

    return {
        "success": True,
        "result": result
    }