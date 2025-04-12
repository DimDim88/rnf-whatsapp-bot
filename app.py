
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

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
    app.run(host="0.0.0.0", port=10000)
