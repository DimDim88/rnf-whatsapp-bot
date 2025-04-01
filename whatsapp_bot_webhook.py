
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get("Body", "").strip().lower()
    response_msg = ""

    if "שלום" in incoming_msg:
        response_msg = (
            "שלום וברוך הבא ל־R&F מטבחים 👋\n"
            "איך נוכל לעזור לך היום?\n"
            "1️⃣ לעצב מטבח בהתאמה אישית\n"
            "2️⃣ לראות דגמים מוכנים לרכישה\n"
            "3️⃣ מבצעים מיוחדים\n"
            "4️⃣ דברו איתי עם נציג"
        )
    elif incoming_msg == "1":
        response_msg = "מצוין! בוא נתחיל בעיצוב המטבח שלך.\nמה סוג המטבח שתרצה? (מודרני, כפרי, קלאסי...)"
    elif incoming_msg == "2":
        response_msg = "הנה הדגמים שלנו: 2 מטר, 3 מטר, עם בילד-אין. כתוב איזה מהם תרצה לראות."
    elif incoming_msg == "3":
        response_msg = "המבצע שלנו: מטבח 2 מטר עם בילדאין ב-₪7,900 בלבד כולל הובלה! רוצה לשמוע עוד?"
    elif incoming_msg == "4":
        response_msg = "אין בעיה 🙏 אעביר את הפרטים שלך לנציג. איך קוראים לך?"
    else:
        response_msg = "לא הבנתי אותך... תוכל לבחור 1, 2, 3 או 4 מהתפריט 😊"

    return f"<Response><Message>{response_msg}</Message></Response>", 200, {"Content-Type": "application/xml"}

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
