from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API working", "endpoint": "/chat"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True, silent=True) or {}

    # Accept both keys so multiple clients can work.
    user_query = (data.get("message") or data.get("question") or "").strip()
    meta = data.get("meta") or {}

    if not user_query:
        return jsonify({"error": "No message provided"}), 400

    persona = meta.get("persona") or "default"
    lang = meta.get("lang") or "English"
    depth = meta.get("depth") or 1

    answer = f"[persona={persona}, lang={lang}, depth={depth}] You said: {user_query}"

    # Provide both fields for compatibility.
    return jsonify({
        "answer": answer,
        "response": answer,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
