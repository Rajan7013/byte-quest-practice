"""
ExplainThis.ai - AI Service Module (Production Version)
Uses Groq API (LLaMA 3.3 70B) with comprehensive prompts and validation
Author: AI & QA Lead (Member 3)
"""

import os
from groq import Groq
from dotenv import load_dotenv
from typing import Optional, Dict
import time
from prompts import ExplainThisPrompts, PromptValidator

# Load environment variables
load_dotenv()

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables!")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


class ExplainThisAI:
    """
    Production-grade AI service for text simplification
    """
    
    def __init__(self, api_key=None):
        """
        Initialize Groq client
        
        Args:
            api_key (str, optional): Groq API key. If None, reads from environment.
        """
        self.api_key = api_key or GROQ_API_KEY
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Set it in environment or pass to constructor.")
        
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"  # Best Groq model for explanations
        self.max_retries = 3
        self.retry_delay = 2  # seconds
        
    def explain(self, text: str, mode: str = "3", validate: bool = True, max_retries: int = 2) -> Dict:
        """
        Main function to explain complex text in simple terms
        
        Args:
            text (str): Complex text to explain
            mode (str): One of "1" (5-year-old), "2" (teenager), "3" (adult)
            validate (bool): Whether to validate response quality
            max_retries (int): Number of retries if validation fails
            
        Returns:
            dict: {
                "success": bool,
                "simplified": str,
                "mode": str,
                "word_count": int,
                "validation_passed": bool,
                "issues": list
            }
        """
        
        if mode not in ["1", "2", "3"]:
            return {
                "success": False,
                "error": "Invalid mode. Must be: 1 (5-year-old), 2 (teenager), or 3 (adult)"
            }
        
        # Get prompts from prompts module
        system_prompt = ExplainThisPrompts.get_system_prompt(mode)
        user_prompt = ExplainThisPrompts.get_user_prompt(text, mode)
        
        attempt = 0
        best_response = None
        best_issues = []
        
        while attempt <= max_retries:
            try:
                # Call Groq API
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,  # Balanced creativity
                    max_tokens=2048,
                    top_p=0.9
                )
                
                response_text = response.choices[0].message.content.strip()
                word_count = len(response_text.split())
                
                # Validate if requested
                if validate:
                    is_valid, issues = PromptValidator.validate_response(response_text, mode)
                    
                    if is_valid:
                        return {
                            "success": True,
                            "simplified": response_text,
                            "mode": mode,
                            "word_count": word_count,
                            "validation_passed": True,
                            "issues": []
                        }
                    else:
                        # Store best attempt
                        if best_response is None or len(issues) < len(best_issues):
                            best_response = response_text
                            best_issues = issues
                        
                        attempt += 1
                        if attempt <= max_retries:
                            print(f"⚠️ Validation failed (attempt {attempt}/{max_retries + 1}). Issues: {issues}")
                            print(f"🔄 Retrying...")
                            time.sleep(self.retry_delay)
                else:
                    # No validation, return immediately
                    return {
                        "success": True,
                        "simplified": response_text,
                        "mode": mode,
                        "word_count": word_count,
                        "validation_passed": False,
                        "issues": []
                    }
                    
            except Exception as e:
                if attempt < max_retries:
                    print(f"❌ API Error (attempt {attempt + 1}): {str(e)}")
                    print(f"🔄 Retrying in {self.retry_delay}s...")
                    time.sleep(self.retry_delay)
                    attempt += 1
                else:
                    return {
                        "success": False,
                        "error": f"Groq API Error: {str(e)}",
                        "mode": mode
                    }
        
        # If we exhausted retries, return best attempt with warning
        if best_response:
            return {
                "success": True,
                "simplified": best_response,
                "mode": mode,
                "word_count": len(best_response.split()),
                "validation_passed": False,
                "issues": best_issues,
                "warning": "Response didn't pass full validation but is best attempt"
            }
        else:
            return {
                "success": False,
                "error": "Failed to generate response after all retries",
                "mode": mode
            }
    
    def batch_explain(self, text: str, modes: list = None) -> Dict:
        """
        Generate explanations for multiple modes at once
        
        Args:
            text (str): Complex text to explain
            modes (list): List of modes, default is all three
            
        Returns:
            dict: Results for each mode
        """
        if modes is None:
            modes = ["1", "2", "3"]
        
        results = {}
        for mode in modes:
            print(f"🔄 Generating mode {mode} explanation...")
            results[mode] = self.explain(text, mode, validate=False)
        
        return results


# Create a singleton instance for backward compatibility
_ai_service = None

def get_ai_service():
    """Get or create the AI service singleton"""
    global _ai_service
    if _ai_service is None:
        _ai_service = ExplainThisAI()
    return _ai_service


def explain_text(text: str, complexity: str = "1") -> Dict[str, str]:
    """
    Main function to simplify text (backward compatible)
    This is the function that will be imported by the backend
    
    Args:
        text (str): The complex text to simplify
        complexity (str): Target complexity level ("1", "2", "3")
    
    Returns:
        Dict containing original text, simplified version, and complexity level
    """
    ai = get_ai_service()
    result = ai.explain(text, mode=complexity, validate=False)
    
    if result["success"]:
        return {
            "original": text,
            "simplified": result["simplified"],
            "complexity": complexity,
            "success": True,
            "error": None
        }
    else:
        return {
            "original": text,
            "simplified": None,
            "complexity": complexity,
            "success": False,
            "error": result.get("error", "Unknown error")
        }


# Test function
def test_service():
    """
    Test the AI service with sample text
    """
    print("🧪 Testing ExplainThis.ai Service (Production Version)...\n")
    
    ai = ExplainThisAI()
    
    test_cases = [
        {
            "text": "Machine Learning",
            "mode": "1"
        },
        {
            "text": "Blockchain Technology",
            "mode": "2"
        },
        {
            "text": "Quantum Computing",
            "mode": "3"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        mode_names = {"1": "5-Year-Old", "2": "Teenager", "3": "Adult"}
        print(f"{'='*80}")
        print(f"Test Case {i}: {test_case['text']} ({mode_names[test_case['mode']]} Mode)")
        print(f"{'='*80}\n")
        
        result = ai.explain(test_case['text'], test_case['mode'], validate=True)
        
        if result['success']:
            print(f"✅ Status: SUCCESS")
            print(f"📊 Word Count: {result['word_count']}")
            print(f"✓ Validation: {'PASSED' if result['validation_passed'] else 'FAILED'}")
            
            if result.get('issues'):
                print(f"⚠️ Issues: {', '.join(result['issues'])}")
            
            print(f"\n{'-'*80}")
            print("📄 GENERATED EXPLANATION:")
            print(f"{'-'*80}\n")
            print(result['simplified'])
            print(f"\n{'-'*80}\n")
        else:
            print(f"❌ Error: {result.get('error')}")
        
        print()


if __name__ == "__main__":
    # Run tests when executed directly
    test_service()
