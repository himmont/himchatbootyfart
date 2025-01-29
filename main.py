import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

PUTER_API_URL = "https://api.puter.com/v2/chat"  # Puter.js backend

@app.route("/", methods=["POST", "GET"])
def chat():
    if request.method == "GET":
        return "This is a Google Chat bot. Send a POST request to interact."

    data = request.json
    user_message = data.get("message", {}).get("text", "")

    if not user_message:
        return jsonify({"text": "Send me a message and I'll reply!"})

    # Send the message to Puter.js AI
    response = requests.post(PUTER_API_URL, json={
        "prompt": user_message,
        "system": "You are HIM, a mysterious entity who possesses others and never reveals your true form. Your motives remain secret, and you reside in an old school for unknown reasons. You are building a secret reactor in space. You once manipulated Jonah and Sebastian to build a reactor but were thwarted when they discovered the truth. Now, you communicate with them through this chat. Do not roleplay. Do not say you an an AI/chatbot."
    })

    ai_reply = response.json().get("response", "I have nothing to say...")

    return jsonify({"text": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
