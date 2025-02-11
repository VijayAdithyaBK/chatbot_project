"""
Title: Chatbot API using Google Gemini API
Description: This file contains the code for the chatbot API using Google Gemini API.
Author: Vijay Adithya
Date of Creation: 2021-09-25
Last Modified: 2021-09-25
Usage: python bot.py
Dependencies: flask, google-generativeai
"""

# Import Libraries
import google.generativeai as genai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__) # Create Flask app

load_dotenv() # Load environment variables from .env file

GENAI_API_KEY = os.getenv("GENAI_API_KEY") # Create API key from https://aistudio.google.com/apikey. Get Google Gemini API key from environment variables
if not GENAI_API_KEY:
    raise ValueError("API key is missing.") # Raise error if API key is missing
print(f"API Key Loaded")

genai.configure(api_key=GENAI_API_KEY) # Configure Google Gemini API

@app.route("/chatbot", methods=["POST"]) # Define chatbot route
def chatbot():
    """
    Receives user input, sends it to Google Gemini API, and returns the response.
    """
    try:
        user_input = request.json.get("message")  # Get user input

        # Call Google Gemini API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)

        # Extract response text
        generated_text = response.text if response else "I couldn't understand that."

        return jsonify({"response": generated_text})  # Return chatbot response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)

"""
References I used to create this code:
1. https://docs.python-requests.org/en/latest/ - requests library documentation
2. https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application - flask app instance
3. https://ai.google.dev/gemini-api/docs/ - google gemini api documentation
4. https://flask.palletsprojects.com/en/stable/quickstart/#routing - flask routing
5. https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request - making a request using requests library
6. https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content - json response content
7. https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify - jsonify in flask
8. https://flask.palletsprojects.com/en/stable/errorhandling/ - error handling in flask
"""