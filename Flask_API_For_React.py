# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
from flask_cors import CORS

from flask import Flask, request, jsonify
# Flask: lightweight Python web framework
# request: used to read data sent from frontend (React)
# jsonify: converts Python dict to JSON response

from CLI_Chatbot import get_chatbot_response
# Reuses our existing chatbot logic (same brain as CLI & Streamlit)

# ---------------------------------------------------
# Create Flask application
# ---------------------------------------------------

app = Flask(__name__)
# Initializes Flask app instance
CORS(app)

# ---------------------------------------------------
# API Route for Chatbot
# ---------------------------------------------------

@app.route("/chat", methods=["POST"])
# Defines an API endpoint: POST /chat
# React frontend will send requests to this URL

def chat():
    # Reads JSON data sent by React
    data = request.json
    # Example received data:
    # { "message": "Hello" }

    user_message = data.get("message")
    # Extracts the user message from JSON

    reply = get_chatbot_response(user_message)
    # Sends user message to chatbot logic
    # Receives AI-generated response

    return jsonify({
        "response": reply
    })
    # Sends chatbot response back to React as JSON

# ---------------------------------------------------
# Run Flask server
# ---------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
    # Starts Flask server on http://localhost:5000
    # debug=True auto-reloads on code changes
