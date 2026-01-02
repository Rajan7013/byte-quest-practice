# ExplainThis.ai - API Documentation

## Base URL

**Local Development:** `http://localhost:8000`  
**Production:** `https://your-render-app.onrender.com` (TBD)

---

## Authentication

Currently, no authentication is required for the `/analyze` endpoint.  
Authentication will be added for `/login` and `/save` endpoints.

---

## Endpoints

### 1. Health Check

**Endpoint:** `GET /`  
**Description:** Check if the API is running

**Response:**
```json
{
  "status": "online",
  "message": "ExplainThis.ai API is running!",
  "ai_service": true
}
```

---

### 2. Detailed Health Check

**Endpoint:** `GET /health`  
**Description:** Detailed system health status

**Response:**
```json
{
  "status": "healthy",
  "message": "All systems operational",
  "ai_service": true
}
```

---

### 3. Analyze Text

**Endpoint:** `POST /analyze`  
**Description:** Simplify complex text using AI

**Request Body:**
```json
{
  "text": "string (required, max 5000 chars)",
  "complexity": "string (optional, default: '5-year-old')"
}
```

**Complexity Options:**
- `5-year-old` - Very simple language for children
- `teenager` - Casual language for teens
- `adult` - Professional but clear language

**Example Request:**
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "The party of the first part shall indemnify and hold harmless the party of the second part from any and all claims arising from negligence.",
    "complexity": "5-year-old"
  }'
```

**Success Response (200):**
```json
{
  "original": "The party of the first part shall indemnify...",
  "simplified": "If something goes wrong because of the first person's mistake, they will pay for it and protect the second person.",
  "complexity": "5-year-old",
  "success": true,
  "error": null
}
```

**Error Responses:**

**400 Bad Request** - Invalid input
```json
{
  "detail": "Text cannot be empty"
}
```

**400 Bad Request** - Text too long
```json
{
  "detail": "Text too long (max 5000 characters)"
}
```

**400 Bad Request** - Invalid complexity
```json
{
  "detail": "Invalid complexity. Must be one of: 5-year-old, teenager, adult"
}
```

**500 Internal Server Error** - AI service error
```json
{
  "detail": "AI service error: [error message]"
}
```

**503 Service Unavailable** - AI service not available
```json
{
  "detail": "AI service not available"
}
```

---

### 4. Login (Coming Soon)

**Endpoint:** `POST /login`  
**Description:** User authentication via Supabase  
**Status:** To be implemented by Backend Lead

**Current Response:**
```json
{
  "message": "Login endpoint - To be implemented by Backend Lead",
  "status": "coming_soon"
}
```

---

### 5. Save History (Coming Soon)

**Endpoint:** `POST /save`  
**Description:** Save explanation to user history  
**Status:** To be implemented by Backend Lead

**Current Response:**
```json
{
  "message": "Save endpoint - To be implemented by Backend Lead",
  "status": "coming_soon"
}
```

---

## Testing Examples

### Example 1: Legal Text

**Request:**
```json
{
  "text": "The party of the first part shall indemnify and hold harmless the party of the second part from any and all claims arising from negligence.",
  "complexity": "5-year-old"
}
```

**Expected Response:**
```json
{
  "simplified": "If something goes wrong because of the first person's mistake, they will pay for it and protect the second person."
}
```

---

### Example 2: Medical Text

**Request:**
```json
{
  "text": "Mitochondria are membrane-bound organelles that generate most of the chemical energy needed to power the cell's biochemical reactions.",
  "complexity": "teenager"
}
```

**Expected Response:**
```json
{
  "simplified": "Mitochondria are like tiny power plants inside your cells that create energy so your body can function."
}
```

---

### Example 3: Technical Text

**Request:**
```json
{
  "text": "A recursive function is a function that calls itself during its execution, typically with a base case to prevent infinite recursion.",
  "complexity": "adult"
}
```

**Expected Response:**
```json
{
  "simplified": "A recursive function is a function that uses itself to solve a problem, breaking it down into smaller parts until it reaches a simple case that stops the process."
}
```

---

## Error Handling

All errors follow the FastAPI standard error format:

```json
{
  "detail": "Error message here"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `500` - Internal Server Error
- `503` - Service Unavailable

---

## Rate Limiting

**Current:** No rate limiting  
**Production:** TBD (will be added before deployment)

---

## CORS Configuration

**Current:** Allows all origins (`*`)  
**Production:** Will be restricted to Vercel frontend domain

---

## Testing with cURL

### Windows (CMD)
```cmd
curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d "{\"text\":\"Test text\",\"complexity\":\"5-year-old\"}"
```

### Linux/Mac
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"Test text","complexity":"5-year-old"}'
```

---

## Testing with Python

```python
import requests

url = "http://localhost:8000/analyze"
data = {
    "text": "Your complex text here",
    "complexity": "5-year-old"
}

response = requests.post(url, json=data)
print(response.json())
```

---

## Notes for Team

- **Frontend Lead (Member 1):** Use the `/analyze` endpoint for the main feature
- **Backend Lead (Member 2):** Implement `/login` and `/save` with Supabase
- **AI Lead (Member 3):** Monitor AI service performance and optimize prompts

---

**Last Updated:** 2026-01-02  
**Version:** 1.0.0
