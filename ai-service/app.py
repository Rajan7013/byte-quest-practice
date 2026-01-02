"""
ExplainThis.ai - Flask Web Server (Production Version)
Minimal web interface for the AI service
Author: AI & QA Lead (Member 3)
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from ai_service import get_ai_service

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Get AI service instance
ai = get_ai_service()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/explain', methods=['POST'])
def api_explain():
    """API endpoint for text explanation"""
    data = request.get_json()
    
    text = data.get('text', '').strip()
    complexity = data.get('complexity', '1')
    
    print(f"📊 Received complexity: {complexity}")  # Debug log
    print(f"📝 Text: {text[:50]}...")  # Debug log
    
    if not text:
        return jsonify({"success": False, "error": "Text cannot be empty"}), 400
    
    # Use the production AI service
    result = ai.explain(text, mode=complexity, validate=False)
    
    if result["success"]:
        return jsonify({
            "success": True,
            "simplified": result["simplified"],
            "word_count": result.get("word_count", 0),
            "mode": result.get("mode", complexity)
        })
    else:
        return jsonify({
            "success": False,
            "error": result.get("error", "Unknown error")
        }), 500

if __name__ == '__main__':
    print("🚀 Starting ExplainThis.ai Web Server (Production Version)...")
    print("📍 Open your browser at: http://localhost:5000")
    print("✅ Using production AI service with validation")
    app.run(debug=True, host='0.0.0.0', port=5000)
