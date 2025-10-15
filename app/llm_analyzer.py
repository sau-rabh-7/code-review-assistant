import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from .models import CodeReviewReport

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API client with your key
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except TypeError:
    # This handles the case where the API key is not set, preventing a crash.
    print("ERROR: GOOGLE_API_KEY environment variable not set.")
    # You might want to exit or raise a more specific error here.

# A mapping to potentially give the model more context, though not strictly necessary
LANGUAGE_MAP = {
    "python": "Python",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "java": "Java",
    "csharp": "C#",
    "go": "Go",
}

def get_llm_review(language: str, code: str) -> CodeReviewReport:
    """
    Sends code to the Google Gemini API for review and returns a structured response.
    """
    # Use gemini-1.5-flash for speed and cost-effectiveness
    model = genai.GenerativeModel('gemini-2.5-flash')

    # The prompt is slightly different for Gemini, but the goal is the same.
    # We are very explicit about the required JSON output.
    prompt = f"""
    You are an expert code reviewer AI. Your task is to analyze the following {LANGUAGE_MAP.get(language, language)} code for readability, modularity, and potential bugs.

    Provide a quantitative score from 1.0 to 10.0 for each category. A score of 10.0 is best for readability/modularity, and 10.0 represents the highest bug potential.

    You must respond ONLY with a valid JSON object that strictly adheres to this structure, with no extra text, explanations, or markdown formatting.
    {{
      "readability_score": float,
      "modularity_score": float,
      "bug_potential": float,
      "overall_summary": "A concise summary of the code's quality.",
      "suggestions": [
        {{
          "line": integer,
          "suggestion": "A specific, actionable improvement suggestion."
        }}
      ]
    }}

    Code to review:
    ```
    {code}
    ```
    """

    print("--- Sending request to Google Gemini API ---")
    
    try:
        # Generate the content
        response = model.generate_content(prompt)
        
        # The response text might be wrapped in markdown backticks, so we clean it
        cleaned_response_text = response.text.strip().replace("```json", "").replace("```", "")
        
        print("--- Received JSON response from Gemini ---")
        print(cleaned_response_text)
        
        # Parse the cleaned JSON string
        review_data = json.loads(cleaned_response_text)
        
        # Validate with Pydantic
        return CodeReviewReport(**review_data)

    except Exception as e:
        print(f"An error occurred while communicating with Gemini or parsing the response: {e}")
        # Re-raise the exception to be handled by FastAPI's error handling
        raise