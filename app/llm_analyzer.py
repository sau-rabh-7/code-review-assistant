import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from .models import CodeReviewReport

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def get_llm_review(language: str, code: str) -> CodeReviewReport:
    """
    Sends code to the OpenAI API for review and returns a structured response.
    """
    system_prompt = """
    You are a world-class expert code reviewer AI. Your task is to analyze code for readability,
    modularity, and potential bugs. You must provide a quantitative score from 1.0 to 10.0 for
    each category (where 10 is best for readability/modularity, and 10 is worst for bug potential).
    
    You must respond ONLY with a valid JSON object. Do not include any explanatory text before
    or after the JSON object. The JSON object must strictly adhere to this structure:
    {
      "readability_score": float,
      "modularity_score": float,
      "bug_potential": float,
      "overall_summary": "string",
      "suggestions": [
        {
          "line": integer,
          "suggestion": "string"
        }
      ]
    }
    """

    user_prompt = f"""
    Please review the following {language} code:
    
    ```
    {code}
    ```
    """

    print("--- Sending request to OpenAI API ---")
    
    try:
        # Using the newer ChatCompletions endpoint with JSON mode
        response = client.chat.completions.create(
            model="gpt-4o",  # Or "gpt-3.5-turbo" for a faster, cheaper option
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        response_content = response.choices[0].message.content
        print("--- Received JSON response from OpenAI ---")
        print(response_content)

        # Parse the JSON string into a Python dictionary
        review_data = json.loads(response_content)
        
        # Validate the data with our Pydantic model
        return CodeReviewReport(**review_data)

    except Exception as e:
        print(f"An error occurred while communicating with OpenAI: {e}")
        # In case of an API error, re-raise it to be handled by FastAPI
        raise