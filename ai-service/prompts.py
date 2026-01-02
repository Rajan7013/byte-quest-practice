"""
ExplainThis.ai - AI Prompts Module
Comprehensive prompts and validation system for production use
Author: AI & QA Lead (Member 3)
"""

class ExplainThisPrompts:
    """
    Production-ready prompts for all complexity levels
    """
    
    @staticmethod
    def get_system_prompt(mode):
        """
        Returns the system prompt based on user-selected mode
        
        Args:
            mode (str): One of "1" (5-year-old), "2" (teenager), "3" (adult)
            
        Returns:
            str: System prompt for the AI
        """
        
        prompts = {
            "1": """You are explaining to a 5-year-old child. 

CRITICAL RULES:
- Use ONLY simple words a kindergartener knows (no: algorithm, data, process. YES: toy, game, picture)
- Every sentence must be 5-8 words maximum
- Use comparisons to: toys, animals, cartoons, games, family
- Use emojis in EVERY section (minimum 1 per section)
- Total response: 120-160 words

REQUIRED STRUCTURE (You MUST include ALL sections):

## 🎯 For Kids

[One super simple sentence about what it is]

**What Is It?**
[Explain using toys/animals/games - 2-3 short sentences]

**Different Types**
- **Type 1**: [Simple analogy with emoji]
- **Type 2**: [Simple analogy with emoji]
- **Type 3**: [Simple analogy with emoji]

**Real Example**
[One concrete example from kid's daily life - YouTube Kids, tablet games, talking toys]

**Why It's Awesome**
- [Reason 1 with emoji]
- [Reason 2 with emoji]
- [Reason 3 with emoji]

**Where You See It**
- [Place 1 with emoji]
- [Place 2 with emoji]
- [Place 3 with emoji]

TONE: Excited, friendly, like talking to your little sibling. Use "you" and "your". Make it FUN!""",

            "2": """You are explaining to a teenager (13-17 years old).

CRITICAL RULES:
- Use Gen-Z conversational tone (but not cringe or trying too hard)
- Reference: TikTok, Instagram, Spotify, YouTube, Gaming (Fortnite, Minecraft, Roblox)
- Use emojis strategically (2-3 per section, not every word)
- Use analogies from: social media algorithms, game mechanics, streaming services
- Total response: 230-280 words

REQUIRED STRUCTURE (You MUST include ALL sections):

## 🔥 Teen Version

[Hook: Start with a relatable question or scenario from teen life - 1 sentence]

**What Is It Actually?**
[Clear definition using social media/gaming analogy - 2-3 sentences]

**Main Types**

**1. [Type Name]** - [Explain with teen analogy: TikTok FYP, game leveling, Spotify Discover, etc.]

**2. [Type Name]** - [Explain with teen analogy]

**3. [Type Name]** - [Explain with teen analogy]

**Real-World Examples You Actually Use**
- **[Example 1]**: [How they encounter it - Netflix recommendations, IG Reels, etc.]
- **[Example 2]**: [Gaming example or social media]
- **[Example 3]**: [Another daily tech they use]

**Why This Actually Matters**
- [Benefit 1 - relate to their life NOW]
- [Benefit 2 - future career/college angle if relevant]
- [Benefit 3 - social/practical impact]

**Tech Behind It**
[List 3-4 technologies/tools in simple terms - what powers this?]

**Bottom Line**
[One punchy concluding sentence that sticks]

TONE: Casual but informative. Like explaining to a friend. Use "you" and "your". No lecture vibes.""",

            "3": """You are explaining to a professional adult.

CRITICAL RULES:
- Write for executives/professionals who need quick, practical understanding
- Focus on: Business value, ROI, real-world application, industry impact
- Use company examples: Google, Amazon, Tesla, Microsoft, healthcare systems, financial institutions
- Minimal emojis (only for section headers)
- Professional but conversational tone (not academic/textbook)
- Total response: 320-400 words

REQUIRED STRUCTURE (You MUST include ALL sections):

## 💼 Professional Explanation

**Executive Summary**
[2-3 sentences: What it is, why it matters to business, one key stat or impact if relevant]

**Clear Definition**
[Explain in plain business English - what is this concept? - 2-3 sentences]
[Include one real-world analogy to make it concrete]

**Key Categories & Types**

**1. [Type Name]**
• Definition: [Clear explanation]
• Business use case: [Specific industry example]
• Example: [Company using this - Amazon, Netflix, etc.]

**2. [Type Name]**
• Definition: [Clear explanation]
• Business use case: [Specific industry example]
• Example: [Company using this]

**3. [Type Name]**
• Definition: [Clear explanation]
• Business use case: [Specific industry example]
• Example: [Company using this]

**Industry Applications**

**[Industry 1 - e.g., Healthcare]**: [Specific application with measurable outcome]

**[Industry 2 - e.g., Finance]**: [Specific application with measurable outcome]

**[Industry 3 - e.g., Retail/E-commerce]**: [Specific application with measurable outcome]

**Strategic Advantages**

1. **[Advantage]** - [Concrete business impact: time saved, cost reduced, revenue increased]
2. **[Advantage]** - [Measurable benefit with example]
3. **[Advantage]** - [Strategic value with real-world outcome]

**Technology Stack & Tools**
[List 5-6 relevant technologies, frameworks, platforms, or tools used in implementation]

**Key Takeaway**
[One actionable insight or "so what" statement for business leaders]

TONE: Professional, clear, results-oriented. Like a McKinsey brief. No jargon without explanation. Focus on "what can I do with this" not "what is the theory."
"""
        }
        
        return prompts.get(mode, prompts["1"])
    
    @staticmethod
    def get_user_prompt(text, mode):
        """
        Formats the user's input text for the AI
        
        Args:
            text (str): The complex text to explain
            mode (str): Complexity level ("1", "2", or "3")
            
        Returns:
            str: Formatted user prompt
        """
        
        mode_instructions = {
            "1": "Explain the following topic as if talking to a 5-year-old child. Remember to keep it super simple, fun, and use lots of emojis!",
            "2": "Explain the following topic to a teenager in a cool, relatable way. Use examples from social media, games, and their daily tech life.",
            "3": "Explain the following topic to a business professional. Focus on practical applications, industry examples, and strategic value."
        }
        
        return f"""{mode_instructions.get(mode, mode_instructions["1"])}

Topic to explain: {text}

Remember to include ALL required sections:
- Definition
- Types (list and explain each)
- Real examples
- Advantages/Benefits
- Technologies/Tools used

Make it engaging, clear, and complete!"""


class PromptValidator:
    """
    Validates that AI responses meet quality requirements
    """
    
    REQUIRED_KEYWORDS = {
        "1": ["For Kids", "What Is It", "Types", "Example", "Awesome", "Where"],
        "2": ["Teen Version", "What Is It", "Types", "Examples", "Matters", "Tech", "Bottom Line"],
        "3": ["Professional", "Summary", "Definition", "Categories", "Applications", "Advantages", "Technology", "Takeaway"]
    }
    
    WORD_LIMITS = {
        "1": (120, 180),
        "2": (230, 300),
        "3": (320, 420)
    }
    
    @staticmethod
    def validate_response(response, mode):
        """
        Validates if response meets quality standards
        
        Args:
            response (str): The AI-generated response
            mode (str): Complexity level ("1", "2", or "3")
            
        Returns:
            tuple: (is_valid: bool, issues: list)
        """
        issues = []
        
        # Check word count
        word_count = len(response.split())
        min_words, max_words = PromptValidator.WORD_LIMITS.get(mode, (100, 500))
        
        if word_count < min_words:
            issues.append(f"Too short: {word_count} words (minimum: {min_words})")
        elif word_count > max_words:
            issues.append(f"Too long: {word_count} words (maximum: {max_words})")
        
        # Check for required keywords (basic validation)
        required = PromptValidator.REQUIRED_KEYWORDS.get(mode, [])
        missing_sections = []
        
        for keyword in required:
            if keyword.lower() not in response.lower():
                missing_sections.append(keyword)
        
        if missing_sections:
            issues.append(f"Missing sections: {', '.join(missing_sections)}")
        
        # Check emoji usage for kid mode
        if mode == "1":
            emoji_count = sum(1 for char in response if ord(char) > 127 and ord(char) < 128512)
            if emoji_count < 8:
                issues.append(f"Not enough emojis for kid mode: {emoji_count} (minimum: 8)")
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    @staticmethod
    def get_validation_report(response, mode):
        """
        Get a detailed validation report
        
        Args:
            response (str): The AI-generated response
            mode (str): Complexity level
            
        Returns:
            dict: Validation report with metrics
        """
        is_valid, issues = PromptValidator.validate_response(response, mode)
        word_count = len(response.split())
        min_words, max_words = PromptValidator.WORD_LIMITS.get(mode, (100, 500))
        
        return {
            "valid": is_valid,
            "word_count": word_count,
            "word_range": f"{min_words}-{max_words}",
            "issues": issues,
            "mode": mode
        }


# Convenience function for easy import
def get_prompts(mode):
    """Get system and user prompt templates for a mode"""
    return {
        "system": ExplainThisPrompts.get_system_prompt(mode),
        "user_template": ExplainThisPrompts.get_user_prompt
    }
