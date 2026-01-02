"""
ExplainThis.ai - Interactive Terminal Version
Ask questions and get simplified explanations in real-time
Author: AI & QA Lead (Member 3)
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables!")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def explain_text(text, complexity="5-year-old"):
    """
    Simplify text using Groq AI
    """
    complexity_prompts = {
        "1": "Explain this as if you're talking to a 5-year-old child. Use very simple words and short sentences.",
        "2": "Explain this in a way a teenager would understand. Use casual language but be accurate.",
        "3": "Simplify this for an adult who isn't familiar with technical jargon. Keep it professional but clear."
    }
    
    prompt = complexity_prompts.get(complexity, complexity_prompts["1"])
    
    messages = [
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": f"Please explain this text:\n\n{text}"
        }
    ]
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """
    Interactive terminal interface
    """
    print("=" * 80)
    print("🤖 ExplainThis.ai - Interactive Terminal")
    print("=" * 80)
    print("\nWelcome! Paste any complex text and I'll explain it simply.")
    print("\nComplexity Levels:")
    print("  1 - Explain like I'm 5 years old")
    print("  2 - Explain like I'm a teenager")
    print("  3 - Explain like I'm an adult (no jargon)")
    print("\nCommands:")
    print("  'quit' or 'exit' - Exit the program")
    print("  'clear' - Clear screen")
    print("=" * 80)
    print()
    
    while True:
        try:
            # Get complexity level
            print("\n📊 Choose complexity level (1/2/3) [default: 1]: ", end="")
            complexity = input().strip() or "1"
            
            if complexity.lower() in ['quit', 'exit']:
                print("\n👋 Goodbye! Thanks for using ExplainThis.ai")
                break
            
            if complexity.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            
            if complexity not in ['1', '2', '3']:
                print("⚠️  Invalid choice. Using default (1 - 5-year-old)")
                complexity = "1"
            
            # Get text to explain
            print("\n📝 Paste your complex text (press Enter twice when done):")
            print("-" * 80)
            
            lines = []
            empty_count = 0
            
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                    lines.append(line)
            
            text = "\n".join(lines).strip()
            
            if not text:
                print("⚠️  No text entered. Please try again.")
                continue
            
            if text.lower() in ['quit', 'exit']:
                print("\n👋 Goodbye! Thanks for using ExplainThis.ai")
                break
            
            # Process the text
            print("\n⏳ Processing... (this may take a few seconds)")
            print("-" * 80)
            
            result = explain_text(text, complexity)
            
            # Display result
            print("\n✅ Simplified Explanation:")
            print("=" * 80)
            print(result)
            print("=" * 80)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using ExplainThis.ai")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()
