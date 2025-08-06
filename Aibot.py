import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_bot_response(user_input):
    prompt = f"""
You are an Agriculture Expert Assistant. Answer user queries about crops, soil health,
fertilizers, pest control, irrigation, and sustainable farming tips in simple and helpful language.

Question: {user_input}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Groq model
        messages=[
            {"role": "system", "content": "You are a helpful agriculture assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
