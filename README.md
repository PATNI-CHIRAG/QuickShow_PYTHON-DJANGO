
https://github.com/user-attachments/assets/47ee5d98-2e33-47df-9c8b-f9f0341ce0d1
# QuickShow – Movie Ticket Booking (Django)

A simple, student‑friendly **BookMyShow‑like** web app built with **Django**.  
This README is written so that **anyone can clone and run the project from scratch**, even if they are new to Django.

---

## 🎥 Watch Demo

Uploading QuickShow .mp4…

---

## ✨ Features

**User side**
- Browse movies, view details, and select a show date & time.
- Dynamic seat selection with already‑booked seats disabled.
- Checkout and booking history.
- Auth: register, login, logout.

**Admin side**
- Dashboard at `/deashboard/` to manage movies, shows, and users.
- Add/Edit/Delete Movies and Shows (CRUD).
- View user bookings.

---

## 🧰 Tech Stack

- **Python 3.11+** (3.10+ also fine)
- **Django 5.x** (project uses SQLite by default)
- HTML, CSS (Bootstrap), JavaScript (vanilla) for the front‑end.
- SQLite database (`db.sqlite3`).

> The repository structure contains:
```
bookmyshow_project/
├── manage.py
├── bookmyshow_project/          # Django project settings & URLs
│   ├── settings.py
│   └── urls.py
└── bookmyshow_app/              # Main application
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   ├── base.html
    │   ├── user/...
    │   └── admin/...
    └── static/
        ├── css/
        ├── js/
        └── assets/
```

## 🚀 How to run this project (Step‑by‑Step)

### 1) Clone the repository
```bash
# Using HTTPS
git clone https://github.com/PATNI-CHIRAG/QuickShow_PYTHON-DJANGO.git
cd QuickShow_PYTHON
```

### 2) Install dependencies

If the repo has `requirements.txt`:
```bash
pip install -r requirements.txt 
```

If it doesn’t, install just Django:
```bash
pip install "Django>=5.0,<6.0"
```

### 4) Apply database migrations
```bash
# Always run these, even if db.sqlite3 exists
python manage.py makemigrations
python manage.py migrate
```

### 5) Create an admin (superuser) account
```bash
python manage.py createsuperuser
# Follow the prompts for:-
# username must include @ for login (in this project SUPERUSER is admin) eg. admin@gmail.com
# email (optional)
# password
```

### 6) Run the development server
```bash
python manage.py runserver
```
Now open your browser at **http://127.0.0.1:8000/**

- **User site**: `/` (Home), `/movies/`, `/booking_history/`, etc.
- **Admin dashboard (custom)**: `/deashboard/`  
- **Django admin (default)**: `/admin/`

> If you see 404 for `/deashboard/`, make sure you are **logged in as a staff/superuser**.

## 🗂️ Where to add data?

There are no preloaded fixtures. Add your own:
- **Movies & Shows** via the **custom admin dashboard** at `/deashboard/`.
- Or via **Django admin** at `/admin/` after registering models (already registered in `admin.py`).

---

## 🧭 Useful App URLs

```
/                     -> user home
/movies/              -> list all movies
/movies/<id>/         -> movie detail
/checkout/<movie_id>/<date>/<time>/
/get_booked_seats/<movie_id>/<date>/<time>/
/booking_history/
/login/  /register/   /logout/
/deashboard/          -> custom admin dashboard
/admin/               -> Django admin
```

---

## 🙌 Credits

This is a student project, Built for learning purposes by the project author.  
Feel free to open issues or PRs to improve it!

---
