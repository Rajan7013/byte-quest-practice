# 🚀 AI Service Setup Instructions

## Quick Setup (3 Steps)

### 1. Install Dependencies

```cmd
cd C:\Users\rajan\.gemini\antigravity\scratch\byte-quest-practice\ai-service
pip install -r requirements.txt
```

### 2. Configure API Key

Edit `.env` file and add your Groq API key:

```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

**Get your key from:** https://console.groq.com/keys

### 3. Test the Service

```cmd
python ai_service.py
```

---

## Expected Output

```
🧪 Testing ExplainThis.ai Service...

Test Case 1:
Complexity: 5-year-old
Original: The party of the first part shall indemnify...
✅ Simplified: [AI-generated simple explanation]
```

---

## Troubleshooting

**Error: "GROQ_API_KEY not found"**
- Make sure `.env` file exists in `ai-service` folder
- Make sure it contains: `GROQ_API_KEY=gsk_...`

**Error: "No module named 'groq'"**
- Run: `pip install -r requirements.txt`

---

## Model Information

- **Provider:** Groq
- **Model:** LLaMA 3.3 70B Versatile
- **Speed:** ~1-2 seconds per request
- **Free Tier:** Generous limits
