# ScholarTrack — Your University Aid & Support Finder

**ScholarTrack** is a personalized AI-powered chatbot that helps students discover financial aid, bursaries, emergency funds, health and wellness resources, and more — all in one place.

Built using **Flask**, **PostgreSQL**, and **Ollama (phi3)**, this tool turns scattered university resources into a smart, searchable assistant that gives you exactly what you need, instantly.

---

## Backstory — Why I Built ScholarTrack

During my second and third year of university, I was battling chronic medical conditions, which made it incredibly difficult to keep up with both school and monthly bills. I often found myself overwhelmed and running out of resources, unaware that my university actually provided support systems for students like me.

Eventually, I learned — after months of struggle — that the University of Alberta offers a wide variety of aid: emergency bursaries, mental health services, food banks, and more. But the problem? These resources were scattered across various websites, forms, and contacts — with no central hub.

That’s when I realized:  
"If it took me this long to find help, how many other students are silently struggling?"

So I built **ScholarTrack** — a simple, student-first chatbot that makes every aid option accessible from one interface.

---

## Features

- Smart LLM Chatbot  
  Uses Ollama’s phi3 model to generate helpful, accurate answers using university data.

- Covers All Aid Types  
  Finance, Food Bank, Career Centre, Health Centre, and Wellness Support — all included.

- Section-Specific Queries  
  Each aid category has its own focused chatbot for more relevant responses.

- PostgreSQL Backend for Scalability  
  Originally built using a static `aid.json`, I migrated the data to PostgreSQL to support dynamic querying, larger data sets, and future university integrations.

- Flask API  
  Simple, modular, and built for fast local inference.

---

## Tech Stack

| Technology       | Purpose                        |
|------------------|--------------------------------|
| Flask (Python)   | Backend API                    |
| PostgreSQL       | Dynamic, scalable database     |
| SQLAlchemy       | ORM to manage DB interactions  |
| Ollama (phi3)    | Lightweight LLM inference      |
| HTML/CSS         | Minimal UI                     |

---
## Demo
![Screenshot 2025-05-12 at 2 23 25 PM](https://github.com/user-attachments/assets/6e7ce158-b751-4e33-9a73-3e6eca86b6c7)

![Screenshot 2025-05-12 at 2 23 38 PM](https://github.com/user-attachments/assets/7e981a21-68a2-4728-a23b-e7bda138cdb4)

<img width="1440" alt="Screenshot 2025-05-12 at 1 12 03 PM (2)" src="https://github.com/user-attachments/assets/1423c9af-9027-46d2-8876-04c740a9756e" />

---
## Future Plans

- Add support for multiple universities  
- Admin dashboard for real-time analytics  
- User login and saved query history  
- Deploy on AWS/GCP for real-time web access

---

## A Note to Fellow Students

If you're reading this while overwhelmed or struggling — I see you.  
This project was built during a time when I had no one to guide me.  
I hope it now becomes a tool that guides you to the help you deserve.

---

## Let’s Connect

- GitHub: [@saherafr](https://github.com/saherafr)
- LinkedIn: https://www.linkedin.com/in/saher-khan-961208216/

## Installation & Dependencies

### 1. Clone the Repository

```bash
git clone https://github.com/saherafr/scholarTrack.git
cd scholarTrack
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
DATABASE_URL=postgresql://username:password@localhost:5432/scholartrack
ollama run phi3
python app.py
---

