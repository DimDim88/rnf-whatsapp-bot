
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
    if not user_input:
        return jsonify({"reply": "שאלה לא התקבלה."})

    prompt = f"""
לקוח שואל: {user_input}
ענה בעברית על פי המחירון הבא:
מטבח ר' 2x2 כולל בילד אין – 6500 ש"ח
מטבח 2x2 – 2500 ש"ח
בילד אין – 2000 ש"ח
אי למטבח – 2900 ש"ח
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": "שגיאה בתקשורת עם GPT", "error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
