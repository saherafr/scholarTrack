import json
import psycopg2

# Load JSON
with open("aid.json") as f:
    data = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="scholartrack",
    user="saherafrinkhan",
    password="",              # leave blank if no password set
    host="localhost"
)
cur = conn.cursor()

for category, items in data.items():  # 'finance' is the category
    for key, section in items.items():  # section = emergency_loan, etc.
        title = section["title"]
        content = "\n".join(section["content"])
        cur.execute(
            "INSERT INTO aid_sections (id, title, content, category) VALUES (%s, %s, %s, %s)",
            (key, title, content, category)
        )


conn.commit()
cur.close()
conn.close()

print("Migration complete ✅")
