
from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    prompt = f"""
לקוח שואל: {user_input}
ענה בעברית על פי המחירון הבא:
מטבח ר' 2x2 כולל בילד אין – 6500 ש"ח
מטבח 2x2 – 2500 ש"ח
בילד אין – 2000 ש"ח
אי למטבח – 2900 ש"ח
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
