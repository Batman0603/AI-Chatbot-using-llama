from flask import Flask, request, jsonify
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TOGETHER_API_KEY")

app = Flask(__name__)
client = Together(api_key=API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": user_message}],
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Runs on port 5000
