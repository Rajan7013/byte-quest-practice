# 🤖 ExplainThis.ai - AI Service Module

## Overview

This is the **AI Service Module** for ExplainThis.ai - the brain of the application that simplifies complex text using Groq's LLaMA 3.3 70B model.

**Author:** Member 3 (AI & QA Lead)

---

## 🎯 What This Module Does

Takes complex text and simplifies it into 3 different complexity levels:
- **Mode 1:** 5-Year-Old (very simple language)
- **Mode 2:** Teenager (casual, relatable)
- **Mode 3:** Adult (professional, clear)

---

## 📁 Files in This Module

| File | Purpose | Used By |
|------|---------|---------|
| `ai_service.py` | Main AI logic | Backend (Member 2) |
| `prompts.py` | AI prompts + validation | `ai_service.py` |
| `test_ai.py` | Test suite | You (for testing) |
| `app.py` | Flask demo server | You (for testing) |
| `interactive.py` | Terminal interface | You (for testing) |
| `INTEGRATION_GUIDE.md` | How to use this module | Backend team |
| `templates/index.html` | Web demo UI | Demo only |

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Setup API Key

Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your key from: https://console.groq.com/keys

### 3. Test It

```bash
# Quick test
python test_ai.py --quick

# Full test suite
python test_ai.py

# Web demo
python app.py
# Then open http://localhost:5000
```

---

## 💻 How to Use (For Backend Team)

### Import the Module

```python
from ai_service import get_ai_service

# Initialize once
ai = get_ai_service()
```

### Call the Function

```python
result = ai.explain(
    text="Machine Learning",
    mode="2",  # "1" = 5-year-old, "2" = teenager, "3" = adult
    validate=False  # Set True for quality validation
)

if result["success"]:
    explanation = result["simplified"]
    word_count = result["word_count"]
else:
    error = result["error"]
```

### Response Format

```python
{
    "success": True,
    "simplified": "## 🔥 Teen Version\n\nMachine learning is...",
    "mode": "2",
    "word_count": 245,
    "validation_passed": False,
    "issues": []
}
```

---

## 🧪 Testing

### Run Tests Before Pushing

```bash
python test_ai.py
```

This will:
- Test all 3 modes
- Validate response quality
- Check word counts
- Generate test report

### Expected Output

```
✅ 5-Year-Old: PASSED (145 words)
✅ Teenager: PASSED (267 words)
✅ Adult: PASSED (358 words)
```

---

## 📊 Architecture

```
ai_service.py
    ↓ imports
prompts.py (ExplainThisPrompts, PromptValidator)
    ↓ uses
Groq API (LLaMA 3.3 70B)
    ↓ returns
Simplified Explanation
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Your Groq API key |

### Model Settings

In `ai_service.py`:
```python
self.model = "llama-3.3-70b-versatile"
self.max_retries = 3
self.retry_delay = 2  # seconds
```

---

## 📝 Prompts

All prompts are in `prompts.py`:

- **5-Year-Old Mode:** Very simple words, short sentences, lots of emojis
- **Teenager Mode:** Casual language, social media references, relatable examples
- **Adult Mode:** Professional language, business examples, strategic focus

Each prompt includes:
- Formatting rules
- Required sections
- Word count targets
- Tone guidelines

---

## ✅ Validation

The `PromptValidator` class checks:
- Word count within range
- Required sections present
- Emoji usage (for kid mode)
- Response quality

---

## 🔄 Integration with Backend

### Step 1: Copy Files

Copy entire `ai-service/` folder to your backend project.

### Step 2: Install Dependencies

```bash
pip install groq==0.13.0 python-dotenv==1.0.0
```

### Step 3: Import in Backend

```python
# In backend/main.py
from ai_service import get_ai_service

ai = get_ai_service()
```

### Step 4: Use in Endpoint

```python
@app.post("/api/explain")
async def explain_endpoint(request):
    result = ai.explain(request.text, mode=request.mode)
    return result
```

See `INTEGRATION_GUIDE.md` for complete examples.

---

## 🎬 Demo

### Web Interface

```bash
python app.py
```

Open http://localhost:5000

Features:
- Text input area
- Mode selector (3 buttons)
- Real-time explanation
- Markdown rendering
- Mobile responsive

### Terminal Interface

```bash
python interactive.py
```

Interactive CLI for quick testing.

---

## 📦 Dependencies

```
groq==0.13.0
python-dotenv==1.0.0
flask==3.0.0
flask-cors==4.0.0
```

---

## 🚫 No Hardcoded Values

✅ All configuration in `.env`  
✅ All prompts in `prompts.py`  
✅ Model name configurable  
✅ Port only in demo (5000)

---

## 🤝 Team Integration

**For Backend (Member 2):**
- Read `INTEGRATION_GUIDE.md`
- Import `ai_service.py`
- Use in FastAPI endpoints

**For Frontend (Member 1):**
- Use backend API endpoint
- Render markdown responses
- Handle loading states

---

## 📚 Documentation

- `INTEGRATION_GUIDE.md` - How to use this module
- `PROJECT_ARCHITECTURE.md` - Complete project overview
- `PRODUCTION_ROADMAP.md` - Development plan

---

## ✨ Features

- ✅ 3 complexity levels
- ✅ Comprehensive prompts
- ✅ Response validation
- ✅ Retry logic
- ✅ Error handling
- ✅ Test suite
- ✅ Web demo
- ✅ Terminal interface

---

## 🎯 Success Criteria

Before pushing to GitHub:
- [ ] All tests pass
- [ ] No hardcoded values
- [ ] Documentation complete
- [ ] Integration guide clear
- [ ] Demo works

---

## 📞 Support

Questions? Contact Member 3 (AI & QA Lead)

---

**Built with ❤️ for Byte Quest Hackathon**
