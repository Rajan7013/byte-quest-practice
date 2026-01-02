# 🔗 ExplainThis.ai - Team Integration Guide

## For Backend Team (Member 2)

### Quick Start

The AI module is now production-ready and easy to integrate!

### 1. Import the AI Service

```python
# In backend/main.py
from ai_service import get_ai_service

# Initialize once (reuse for all requests)
ai = get_ai_service()
```

### 2. Use in Your API Endpoint

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ExplainRequest(BaseModel):
    text: str
    mode: str = "3"  # "1" = 5-year-old, "2" = teenager, "3" = adult

@app.post("/api/explain")
async def explain_endpoint(request: ExplainRequest):
    """
    Main endpoint for text explanation
    """
    result = ai.explain(request.text, mode=request.mode, validate=False)
    
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result.get("error"))
    
    return {
        "explanation": result["simplified"],
        "word_count": result["word_count"],
        "mode": result["mode"]
    }
```

### 3. API Response Format

```json
{
  "success": true,
  "simplified": "Full explanation text here...",
  "mode": "2",
  "word_count": 245,
  "validation_passed": false,
  "issues": []
}
```

### 4. Error Handling

```python
if not result["success"]:
    # Handle error
    error_message = result.get("error", "Unknown error")
    # Log or return to frontend
```

### 5. Supabase Integration (Optional)

```python
# Save to database
await supabase.table("explanations").insert({
    "user_id": user_id,
    "original_text": request.text,
    "simplified_text": result["simplified"],
    "complexity_mode": request.mode,
    "word_count": result["word_count"],
    "created_at": datetime.now()
})
```

---

## For Frontend Team (Member 1)

### API Contract

**Endpoint:** `POST /api/explain`

**Request:**
```json
{
  "text": "Complex text to explain",
  "mode": "2"
}
```

**Response (Success):**
```json
{
  "explanation": "Formatted markdown text...",
  "word_count": 250,
  "mode": "2"
}
```

**Response (Error):**
```json
{
  "error": "Error message here"
}
```

### Mode Values

- `"1"` - 5-Year-Old (very simple language)
- `"2"` - Teenager (casual, relatable)
- `"3"` - Adult (professional, clear)

### Example Frontend Code (React)

```javascript
const explainText = async (text, mode) => {
  const response = await fetch('/api/explain', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text, mode })
  });
  
  const data = await response.json();
  
  if (data.explanation) {
    // Render markdown
    return data.explanation;
  } else {
    // Handle error
    console.error(data.error);
  }
};
```

---

## Testing the AI Module

### Quick Test
```bash
cd ai-service
python test_ai.py --quick
```

### Full Test Suite
```bash
python test_ai.py
```

### Test Web Interface
```bash
python app.py
# Open http://localhost:5000
```

---

## File Structure

```
ai-service/
├── ai_service.py          # Core AI logic (import this)
├── prompts.py             # Prompts + validation
├── test_ai.py             # Test suite
├── app.py                 # Flask demo (reference)
├── requirements.txt       # Dependencies
└── .env                   # API keys
```

---

## Dependencies

Add to your `backend/requirements.txt`:

```
groq==0.13.0
python-dotenv==1.0.0
```

---

## Environment Variables

Required in `.env`:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your key from: https://console.groq.com/keys

---

## Questions?

Tag @Member3 (AI & QA Lead) in Slack/Discord!
