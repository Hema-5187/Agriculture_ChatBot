import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def get_agriculture_reply(user_input):
    """
    Send user query to Groq API and return agriculture-focused response.
    """
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": (
                "You are an Agriculture Assistant Bot. "
                "Provide expert advice about farming, crops, soil health, irrigation, pest control, "
                "weather forecasts, and sustainable agriculture practices. "
                "Avoid unrelated topics."
            )},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
