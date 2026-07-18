import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not api_key:
    raise ValueError(
        "Gemini API key not found. Please add GEMINI_API_KEY to your .env file."
    )

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_response(prompt):
    """
    Generates a response from the Gemini AI model.

    Parameters:
        prompt (str): The prompt sent to Gemini.

    Returns:
        str: The generated response.
    """
    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"