from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get('msg')
    if user_message in ['What is your name?', 'name?']:
        response = "My name is ChatBot."
    elif user_message in ['How old are you?', 'age?']:
        response = "I don't have an age, I'm just a computer program."
    else:
        api_key = "api-key"
        model = "text-curie-001"
        response = generate_response_gpt3(user_message, model, api_key)
    return response

def generate_response_gpt3(user_message, model, api_key):
    prompt = (f"User: {user_message}\n"
              f"ChatBot:")
    response = requests.post(
        "https://api.openai.com/v1/engines/text-curie-001/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.7,
        },
    ).json()

    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    app.run()
