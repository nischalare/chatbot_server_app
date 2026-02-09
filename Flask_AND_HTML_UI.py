# ============================================================
# Flask_AND_HTML_UI.py
# Project: OpenAI_API_Python
# Course: Designing Conversational AI
#
# Purpose:
# This file creates a web-based chatbot interface using:
# - Flask (backend framework)
# - HTML templates (frontend)
#
# It connects the web UI to the SAME chatbot logic
# used by CLI and other interfaces.
#
# IMPORTANT:
# This file handles ONLY UI + request routing.
# AI logic remains in CLI_Chatbot.py (single AI brain).
# ============================================================


# ------------------------------------------------------------
# Import required libraries
# ------------------------------------------------------------

from flask import Flask, render_template, request
# Flask        -> Creates the web server
# render_template -> Renders HTML files from /templates folder
# request      -> Reads user input sent from HTML form

from CLI_Chatbot import get_chatbot_response
# Imports chatbot logic
# This ensures Flask UI reuses the SAME AI brain
# No duplication of OpenAI logic


# ------------------------------------------------------------
# Create Flask application instance
# ------------------------------------------------------------

app = Flask(__name__)
# Initializes the Flask web application
# Flask uses this object to route requests and responses


# ------------------------------------------------------------
# Define Route for Home Page
# ------------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
# "/" represents the root URL (homepage)
# GET  -> Loads the page initially
# POST -> Handles form submission from HTML

def home():
    """
    This function:
    - Displays the chatbot page
    - Accepts user input from the HTML form
    - Sends input to chatbot logic
    - Displays AI-generated response
    """

    response = ""
    # Initializes empty response variable
    # Prevents errors before first user input

    if request.method == "POST":
        # Checks if the form was submitted

        user_input = request.form["message"]
        # Reads user message from HTML input field
        # 'message' comes from <input name="message">

        response = get_chatbot_response(user_input)
        # Sends user input to chatbot logic
        # Receives AI-generated response

    return render_template("index.html", response=response)
    # Renders index.html
    # Passes chatbot response to HTML template
    # Jinja template displays response dynamically


# ------------------------------------------------------------
# Run Flask Application
# ------------------------------------------------------------

if __name__ == "__main__":
    # Ensures this file runs only when executed directly
    # Prevents accidental execution during imports

    app.run(debug=True)
    # Starts Flask development server
    # debug=True enables:
    # - Auto-reload on code changes
    # - Detailed error messages
