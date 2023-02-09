from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get('msg')
    api_key = "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"
    model = "text-davinci-002"
    response = generate_response_gpt3(user_message, model, api_key)
    return response

def generate_response_gpt3(user_message, model, api_key):
    prompt = (f"User: {user_message}\n"
              f"ChatBot:")
    response = requests.post(
        "https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "prompt": prompt,
            "max_tokens": 100,
            "temperature": 0.7,
        },
    ).json()

    return response['choices'][0]['text'].strip()[len(prompt):]

if __name__ == "__main__":
    app.run()
