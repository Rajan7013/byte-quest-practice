"""
ExplainThis.ai - Backend API
FastAPI backend with Gemini AI integration and Supabase
Author: Backend & DB Lead (Member 2) + AI Lead (Member 3)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
import sys

# Add ai-service to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ai-service'))

try:
    from ai_service import explain_text
except ImportError:
    print("⚠️ Warning: ai_service not found. Make sure ai-service folder exists.")
    explain_text = None

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="ExplainThis.ai API",
    description="AI-powered text simplification service",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your Vercel domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class AnalyzeRequest(BaseModel):
    text: str
    complexity: Optional[str] = "5-year-old"


class AnalyzeResponse(BaseModel):
    original: str
    simplified: str
    complexity: str
    success: bool
    error: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    message: str
    ai_service: bool


# Routes
@app.get("/", response_model=HealthResponse)
async def root():
    """
    Health check endpoint
    """
    return {
        "status": "online",
        "message": "ExplainThis.ai API is running!",
        "ai_service": explain_text is not None
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Detailed health check
    """
    return {
        "status": "healthy",
        "message": "All systems operational",
        "ai_service": explain_text is not None
    }


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_text(request: AnalyzeRequest):
    """
    Analyze and simplify text using AI
    
    Args:
        request: AnalyzeRequest with text and complexity level
    
    Returns:
        AnalyzeResponse with simplified text
    """
    
    # Validate input
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if len(request.text) > 5000:
        raise HTTPException(status_code=400, detail="Text too long (max 5000 characters)")
    
    # Validate complexity level
    valid_complexities = ["5-year-old", "teenager", "adult"]
    if request.complexity not in valid_complexities:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid complexity. Must be one of: {', '.join(valid_complexities)}"
        )
    
    # Check if AI service is available
    if explain_text is None:
        raise HTTPException(status_code=503, detail="AI service not available")
    
    try:
        # Call AI service
        result = explain_text(request.text, request.complexity)
        
        if not result['success']:
            raise HTTPException(status_code=500, detail=f"AI service error: {result['error']}")
        
        return AnalyzeResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.post("/login")
async def login():
    """
    User login endpoint
    TODO: Implement Supabase authentication
    """
    return {
        "message": "Login endpoint - To be implemented by Backend Lead",
        "status": "coming_soon"
    }


@app.post("/save")
async def save_history():
    """
    Save explanation to history
    TODO: Implement Supabase database integration
    """
    return {
        "message": "Save endpoint - To be implemented by Backend Lead",
        "status": "coming_soon"
    }


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
