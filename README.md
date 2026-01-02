# 🤖 ExplainThis.ai

> **Simplify complex text into easy-to-understand language using AI**

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Hackathon](https://img.shields.io/badge/Hackathon-Byte%20Quest-blue)

---

## 📋 Project Overview

**ExplainThis.ai** is an AI-powered tool that transforms complex text (legal contracts, medical reports, technical documentation) into simple, easy-to-understand language.

---

## 👥 Team Members

| Role | Name | GitHub | Responsibilities |
|------|------|--------|-----------------|
| **Frontend Lead** | Member 1 | [@username1](https://github.com/username1) | React UI, Vercel Deployment |
| **Backend & DB Lead** | Member 2 | [@username2](https://github.com/username2) | FastAPI, Supabase, Render Deployment |
| **AI & QA Lead** | Member 3 | [@rb4921685-code](https://github.com/rb4921685-code) | Gemini Integration, Testing, Demo |

---

## 🚀 Features

- ✅ **AI-Powered Simplification** - Uses Groq LLaMA 3.3 70B (Production-Ready)
- ✅ **Multiple Complexity Levels** - Explain like I'm 5, teenager, or adult
- ✅ **Comprehensive Prompts** - Detailed, validated prompts for each mode
- ✅ **Quality Validation** - Automated response quality checks
- ✅ **Test Suite** - Comprehensive testing before deployment
- 🔄 **User Authentication** - Secure login via Supabase (Coming Soon)
- 🔄 **History Tracking** - Save and review past explanations (Coming Soon)
- ✅ **Fast & Responsive** - Optimized for speed with retry logic
- ✅ **Modern UI** - Clean, mobile-responsive interface with markdown rendering

---

## 🏗️ Architecture

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Frontend  │─────▶│   Backend   │─────▶│  Groq API   │
│   (React)   │      │  (FastAPI)  │      │ (LLaMA 3.3) │
└─────────────┘      └─────────────┘      └─────────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │  Supabase   │
                     │  (Database) │
                     └─────────────┘
```

---

## 📁 Project Structure

```
byte-quest-practice/
├── frontend/              # React + Vite (Member 1)
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/               # FastAPI (Member 2)
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── ai-service/            # Groq AI Integration (Member 3) ✅ PRODUCTION-READY
│   ├── ai_service.py      # Main AI logic
│   ├── prompts.py         # Comprehensive prompts + validation
│   ├── test_ai.py         # Test suite
│   ├── app.py             # Flask demo
│   ├── interactive.py     # Terminal interface
│   ├── requirements.txt
│   ├── README.md          # AI module documentation
│   ├── INTEGRATION_GUIDE.md
│   └── templates/
│       └── index.html     # Web demo UI
├── docs/                  # Documentation
│   ├── API_DOCUMENTATION.md
│   └── PROJECT_ARCHITECTURE.md  # Complete project guide
└── README.md
```

---

## 🛠️ Tech Stack

### Frontend
- **Framework:** React + Vite
- **Styling:** Tailwind CSS
- **Deployment:** Vercel

### Backend
- **Framework:** FastAPI (Python)
- **Database:** Supabase (PostgreSQL)
- **Deployment:** Render

### AI Service (Production-Ready ✅)
- **Model:** Groq LLaMA 3.3 70B Versatile
- **API:** Groq API
- **Features:** Validation, retry logic, comprehensive prompts
- **Testing:** Automated test suite

---

## 🔧 Setup Instructions

### Prerequisites
- Python 3.9+
- Git
- Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

### 1. Clone the Repository

```bash
git clone https://github.com/rb4921685-code/byte-quest-practice.git
cd byte-quest-practice
```

### 2. AI Service Setup (Member 3) ✅ PRODUCTION-READY

```bash
cd ai-service
pip install -r requirements.txt
```

Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
```

Get your key from: https://console.groq.com/keys

Test the service:
```bash
# Quick test
python test_ai.py --quick

# Full test suite
python test_ai.py

# Web demo
python app.py
```

**Documentation:**
- `ai-service/README.md` - Module documentation
- `ai-service/INTEGRATION_GUIDE.md` - How backend uses it
- `docs/PROJECT_ARCHITECTURE.md` - Complete project guide

### 3. Backend Setup (Member 2)

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

Run the server:
```bash
uvicorn main:app --reload
```

### 4. Frontend Setup (Member 1)

```bash
cd frontend
npm install
npm run dev
```

---

## 📡 API Endpoints

### `GET /`
Health check endpoint

**Response:**
```json
{
  "status": "online",
  "message": "ExplainThis.ai API is running!",
  "ai_service": true
}
```

### `POST /analyze`
Analyze and simplify text using AI.

**Request:**
```json
{
  "text": "The party of the first part shall indemnify...",
  "complexity": "5-year-old"
}
```

**Response:**
```json
{
  "original": "The party of the first part...",
  "simplified": "If something goes wrong, the first person will pay for it.",
  "complexity": "5-year-old",
  "success": true
}
```

**Complexity Levels:**
- `5-year-old` - Very simple language
- `teenager` - Casual but accurate
- `adult` - Professional but clear

---

## 🧪 Testing

### Test AI Service
```bash
cd ai-service
python ai_service.py
```

### Test Backend API
```bash
# Start the server
cd backend
uvicorn main:app --reload

# In another terminal, test the endpoint
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Mitochondria are the powerhouse of the cell\",\"complexity\":\"5-year-old\"}"
```

---

## 🔄 Git Workflow

### Starting Work
```bash
git checkout main
git pull origin main
git checkout -b feature-name
```

### Committing Changes
```bash
git add .
git commit -m "Description of changes"
git push origin feature-name
```

### Creating Pull Request
1. Go to GitHub
2. Click "Compare & pull request"
3. Add description
4. Request review from AI Lead (Member 3)

---

## 🌐 Deployment

### Backend (Render)
- **Status:** Coming Soon
- **URL:** TBD

### Frontend (Vercel)
- **Status:** Coming Soon
- **URL:** TBD

---

## 📝 Current Status

- ✅ **AI Service Module Complete (Production-Ready)**
  - Comprehensive prompts for 3 modes
  - Validation system
  - Test suite
  - Integration documentation
- ✅ Backend API Structure Complete
- 🔄 Frontend Development (In Progress)
- 🔄 Supabase Integration (Pending)
- 🔄 Deployment (Pending)

---

## 🙏 Acknowledgments

- Google Gemini AI
- Byte Quest Hackathon Organizers

---

**Built with ❤️ during Byte Quest Hackathon**
