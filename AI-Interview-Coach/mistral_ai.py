from openai import OpenAI

# ==========================
# Mistral AI Configuration
# ==========================

client = OpenAI(
    api_key="Y6J2m09lHeIXM9kuqRagsz4ApYJ3wMjH",
    base_url="https://api.mistral.ai/v1"
)

# ==========================
# Generate AI Response
# ==========================

def generate_ai_response(prompt):
    """
    Generates a response using the Mistral AI model.

    Parameters:
        prompt (str): The prompt to send to Mistral.

    Returns:
        str: The generated response.
    """
    try:
        response = client.chat.completions.create(
            model="mistral-small-latest",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI interview coach who generates technical interview questions, ideal answers, and interview tips."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"