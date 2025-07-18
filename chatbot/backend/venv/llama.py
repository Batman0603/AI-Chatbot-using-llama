from together import Together
from dotenv import load_dotenv
import os

def get_bot_response(prompt: str) -> str:
    """
    Sends a prompt to the Together API and returns the bot's response.
    """
    try:
        # Load environment variables
        load_dotenv()
        API_KEY = os.getenv("TOGETHER_API_KEY")
        if not API_KEY:
            raise ValueError("TOGETHER_API_KEY is not set in the .env file.")
        
        # Initialize Together client
        client = Together(api_key=API_KEY)

        # Send request to the model
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        # Return the bot's response
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error fetching bot response: {e}")
        return "Sorry, I couldn't process your request. Please try again."