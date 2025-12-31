from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "API working"}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return {
        "question": data.get("question"),
        "answer": "Hello from Render Flask API"
    }

if __name__ == "__main__":
    app.run()
