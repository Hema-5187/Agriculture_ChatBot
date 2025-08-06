from flask import Flask, render_template, request, jsonify
from Aibot import get_agriculture_reply

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Agriculture UI

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    bot_reply = get_agriculture_reply(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
