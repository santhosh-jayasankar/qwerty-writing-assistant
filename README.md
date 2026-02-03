✨ Qwerty – Writing Assistant Web App

Qwerty is a full-stack writing assistant web application that provides Grammar Correction, Translation, and Rephrasing tools through a clean and user-friendly interface.
The project is built to demonstrate real-world backend, deployment, and integration skills, not just UI.

🚀 Live Demo

🔗 Live URL:
https://qwerty-writing-assistant.onrender.com

⚠️ Note: The app runs on a free hosting tier. The first request may take a few seconds due to cold start.

🧠 Features
✍️ Grammar Correction

Corrects grammatical mistakes in English text

Uses LanguageTool public server 

Lightweight and suitable for low-resource hosting

🌐 Translation Tool

Translates text between multiple languages

Built using googletrans

Simple and fast for common use cases

🔁 Rephrasing Tool

Generates alternative sentence rewrites

Uses Sapling API

Designed to improve clarity and tone

👤 User Authentication

User signup & login

Secure session-based authentication

Each user has a personal profile

📜 Tool History

Logged-in users can view their past grammar, translation, and rephrasing results

Stored using Django models

🛠️ Tech Stack
Frontend

HTML5

CSS3

Bootstrap

JavaScript

Backend

Python

Django

Gunicorn

APIs & Services

LanguageTool (Public Server) – Grammar correction (rule-based)

Sapling API – Rephrasing

Googletrans – Translation

Deployment

Docker

Render (Free Tier)

WhiteNoise (static files)

🧩 Architecture Overview
Browser (User)
   ↓
Django Views (Render Server)
   ↓
External Services
   ├─ LanguageTool (Grammar)
   ├─ Sapling API (Rephrasing)
   └─ Google Translate (Translation)


All API calls are handled server-side

No API keys exposed to the frontend

🔐 Environment Variables

The following environment variables are used:

SECRET_KEY=your_django_secret_key
DEBUG=False
SAPLING_API_KEY=your_sapling_api_key


Environment variables are managed securely via Render dashboard.

🐳 Docker Setup (Production)

The application is containerized using Docker.

Dockerfile highlights:

Lightweight Python base image

No Java runtime (to avoid memory issues)

Single Gunicorn worker for free-tier stability

Automatic static file collection and migrations

📦 Dependency Management

The project includes some unused dependencies from earlier experiments.

These do not affect functionality.

For production cleanup, a fresh virtual environment and regenerated requirements.txt is recommended.

This project prioritizes functionality and deployment stability for portfolio demonstration.

⚠️ Known Limitations

Grammar correction uses LanguageTool public server, which:

Has no SLA

May be rate-limited

Is intended only for demo / portfolio use

For production, LanguageTool Cloud API or a dedicated service is recommended.

💡 What This Project Demonstrates

Full-stack Django development

Real deployment debugging (CSRF, ALLOWED_HOSTS, migrations, memory limits)

API integration and trade-off decisions

Dockerized production setup

Clean separation of frontend, backend, and services

🧪 Local Setup (Optional)
git clone https://github.com/your-username/qwerty-writing-assistant.git
cd qwerty-writing-assistant

python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver


Open:
http://127.0.0.1:8000

🧑‍💻 Author

Santhosh J
Aspiring Backend / Full-Stack Developer

📌 Final Note

This project was built as a learning-oriented, interview-ready portfolio application, focusing on practical engineering decisions rather than over-engineering.