import psycopg2

# Data collected manually and structured from UAlberta official websites
bulk_data = [
    {
        "id": "wellness_supports",
        "title": "🧠 Wellness Supports",
        "category": "wellness",
        "content": [
            "Provides mental health and well-being education for students.",
            "Offers peer support programs and guided workshops.",
            "Delivers confidential individual support through mental health advisors.",
            "Connects students with campus-wide wellness resources and events.",
            "Helps reduce stigma and foster resilience across campus.",
            "Hosts Well-being Webinars, Community Care events, and Self-care sessions.",
            "Crisis resources and urgent supports are also available.",
            "More Info: https://www.ualberta.ca/current-students/wellness-supports/index.html"
        ]
    },
    {
        "id": "campus_foodbank",
        "title": "🍎 Campus Food Bank",
        "category": "foodbank",
        "content": [
            "Provides food hampers to UAlberta students and staff in need.",
            "Hampers include fresh produce, grains, proteins, snacks, and canned items.",
            "Offers grocery bus tours to teach affordable food shopping.",
            "Hosts community kitchens and cooking classes.",
            "Offers breakfast programs and free campus snacks.",
            "Emergency hamper pickup is available without an appointment.",
            "More Info: https://campusfoodbank.com/"
        ]
    },
    {
        "id": "career_centre",
        "title": "💼 Career Centre",
        "category": "career",
        "content": [
            "Provides one-on-one advising for job search, career planning, and networking.",
            "Reviews resumes, cover letters, and LinkedIn profiles.",
            "Hosts job fairs and employer sessions throughout the year.",
            "Supports internship and co-op opportunities across faculties.",
            "Offers job board and MyJobBoard portal for verified listings.",
            "Helps students develop transferable skills and confidence.",
            "More Info: https://www.ualberta.ca/career-centre/"
        ]
    },
    {
        "id": "health_services",
        "title": "🏥 University Health Centre",
        "category": "health",
        "content": [
            "Provides full general medical care for students and their families.",
            "Walk-in and appointment-based care for illness, injury, and checkups.",
            "Offers vaccinations, STI screening, and women’s health.",
            "Access to OB/GYN, dermatology, and chronic condition support.",
            "Can provide documentation for academic accommodations.",
            "Operated by licensed physicians and nurses.",
            "More Info: https://www.ualberta.ca/services/health-centre/index.html"
        ]
    },
    {
        "id": "financial_overview",
        "title": "💰 Financial Aid Overview",
        "category": "finance",
        "content": [
            "The university offers scholarships, bursaries, and emergency loans.",
            "Students can access domestic and international supplementary bursaries.",
            "Application support and income documentation may be required.",
            "Bear Tracks is used for aid acceptance and status tracking.",
            "Student Service Centre provides help with eligibility and deadlines.",
            "Graduate students can also apply for GSA emergency bursary.",
            "More Info: https://www.ualberta.ca/registrar/scholarships-awards-financial-support/index.html"
        ]
    }
]

# Database connection setup
conn = psycopg2.connect(
    dbname="scholartrack",
    user="saherafrinkhan",
    host="localhost"
)
cur = conn.cursor()

# Insert each section
for section in bulk_data:
    cur.execute("""
        INSERT INTO aid_sections (id, title, content, category)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            title = EXCLUDED.title,
            content = EXCLUDED.content,
            category = EXCLUDED.category;
    """, (
        section["id"],
        section["title"],
        "||".join(section["content"]),
        section["category"]
    ))

conn.commit()
cur.close()
conn.close()
print("✅ Bulk insert completed.")
