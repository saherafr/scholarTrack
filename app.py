from flask import Flask, render_template, request, jsonify
import psycopg2
import requests
import ast

app = Flask(__name__)

# Section-to-key mapping
SECTION_MAP = {
    "finance": [
        "emergency_loan", "domestic_supplementary_bursary",
        "international_supplementary_bursary", "gsa_emergency_bursary",
        "indigenous_students_support_fund", "advisor_tips"
    ],
    "foodbank": ["campus_foodbank"],
    "career": ["career_centre"],
    "health": ["health_services"],
    "wellness": ["wellness_supports"]
}

# PostgreSQL fetch function
def get_aid_sections(keys):
    conn = psycopg2.connect(
        dbname="scholartrack",
        user="saherafrinkhan",
        host="localhost"
    )
    cur = conn.cursor()
    placeholders = ','.join(['%s'] * len(keys))
    query = f"SELECT title, content FROM aid_sections WHERE id IN ({placeholders})"
    cur.execute(query, keys)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    formatted = []
    for title, content in rows:
        try:
            lines = ast.literal_eval(content) if isinstance(content, str) else content
        except Exception:
            lines = [content]
        formatted.append(f"{title}\n" + "\n".join(f"- {line.strip()}" for line in lines))
    return formatted

# Routes
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/chat/<section>')
def chat(section):
    section = section.lower()
    if section not in SECTION_MAP:
        return render_template('404.html'), 404
    return render_template('chat.html', section=section)

@app.route('/chatbot/<section>', methods=['POST'])
def chatbot(section):
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    keys = SECTION_MAP.get(section, ["advisor_tips"])
    knowledge = "\n\n".join(get_aid_sections(keys))

    prompt = f"""
You are ScholarTrackBot — a friendly, intelligent university assistant trained to help students with {section.upper()} support. Respond conversationally, not like a textbook.

Instructions:
- Be warm and direct in 2–3 sentences max.
- If a student’s question is unclear (like “help with tuition”), ask one short follow-up: “Are you a domestic or international student?” or similar.
- If you mention resources, briefly say what they do and how to access them — don’t list phone numbers unless explicitly asked.
- Avoid big paragraphs or formal tone. Speak like a helpful peer who knows the system well.

Here's your verified knowledge base:
{knowledge}

Student asked: "{user_input}"

Your helpful answer:
"""




    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        })
        reply = res.json().get("response", "Sorry, I couldn't generate a response.")
    except Exception as e:
        reply = "ScholarTrackBot is unavailable right now. Please try again later."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
