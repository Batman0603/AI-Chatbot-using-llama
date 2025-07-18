from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from llama import get_bot_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/chat/', methods=['POST'])
def chat():
    """
    Endpoint to handle chat requests from the frontend.
    """
    try:
        # Get the user's message from the request body
        data = request.json
        user_message = data.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Get the bot's response using the Together API
        bot_response = get_bot_response(user_message)
        
        # Return the bot's response
        return jsonify({"reply": bot_response})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)