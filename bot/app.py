import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    
    [
        r"what is your name ?",
        ["My name is Chatbot", "I'm Chatbot, nice to meet you!"]
    ],
    
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", "Its fine"]
    ],
    
    [
        r"i am fine",
        ["Great to hear that!", "Alright :)"]
    ],
    
    [
        r"quit",
        ["Bye bye take care. See you soon :) "]
    ],
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["text"]
    response = chatbot.respond(message)
    return response

if __name__ == "__main__":
    app.run()
