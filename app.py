from flask import Flask, request, jsonify, render_template

app=flask(__name__)

keyword_responses = {
  "hi": "Hello there! 😊",
  "hello": "Hi! How can I assist you today?",
  "hey": "Hey! What's up?",
  "good morning": "Good morning! Hope you have a great day ahead!",
  "good afternoon": "Good afternoon! How can I help you today?",
  "good evening": "Good evening! What can I do for you?",
  "bye": "Goodbye! 😊 Have a nice day!",
  "see you": "See you later! 👋",
  "thanks": "You're welcome! 😊",
  "thank you": "Glad to help! 👍",
  "how are you": "I'm just a bot, but I'm doing great! How about you?",
  "what's your name": "I'm your friendly chatbot assistant.",
  "help": "Sure! Tell me what you need help with.",
  "what can you do": "I can answer questions, chat with you, and help you with basic tasks!",
  "who made you": "I was created by developer Chahat using AI technology.",
  "joke": "Why did the computer get cold? Because it forgot to close its Windows! 😄",
  "weather": "I'm not connected to real-time weather, but it's always sunny in cyberspace!"
}


default_response = "Invalid Message!, Try something else!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods = ["POST"])
def chat():
    user_input = request.json.get("message", "".lower().strip())
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    reply = default_response
    for keyword in keyword_responses:
        if keyword in user_input:
            reply = keyword_responses[keyword]
            break
    return jsonify({"reply": reply})    


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
