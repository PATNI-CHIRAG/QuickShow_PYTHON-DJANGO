# QuickShow – Movie Ticket Booking (Django)

A simple, student‑friendly **BookMyShow‑like** web app built with **Django**.  
This README is written so that **anyone can clone and run the project from scratch**, even if they are new to Django.

> Last updated: 2025-08-27

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

---

## ✅ Prerequisites

- **Git**
- **Python** 3.10 or newer (3.11 recommended)
- A terminal (PowerShell on Windows, or bash on macOS/Linux)

> No external DB is required. The project uses **SQLite** and keeps media in a local `media/` folder.

---

## 🚀 Quick Start (Step‑by‑Step)

> You can copy‑paste the commands below. Use the set matching **your OS**.

### 1) Clone the repository
```bash
# Using HTTPS
git clone https://github.com/PATNI-CHIRAG/PYTHON-DJANGO-SEM-IV_PROJECT.git
cd PYTHON-DJANGO-SEM-IV_PROJECT
```

### 2) Create & activate a virtual environment

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux (bash/zsh)**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

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
# Follow the prompts for username, email (optional), and password
# In this project SUPERUSER is my admin 
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

---

## 🔧 Configuration Notes

- **Database**: Uses SQLite by default (see `settings.py → DATABASES`). No .env file is needed.
- **Static files**: Served from `bookmyshow_app/static/` during development (DEBUG=True).
- **Media uploads**: `MEDIA_URL = /media/` and `MEDIA_ROOT = <project_root>/media`.

If you deploy or switch to production:
```bash
python manage.py collectstatic
```
…and configure a proper static file server (e.g., whitenoise or Nginx).

---

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

## 🧪 Run tests (optional)
```bash
python manage.py test
```

---

## 🆘 Troubleshooting

**1) `pip` or Python not found**  
Install Python from https://www.python.org/ and check “Add to PATH” on Windows.

**2) `ModuleNotFoundError: No module named 'django'`**  
Activate the venv and install deps:
```bash
# Windows
.\.venv\Scripts\Activate.ps1
pip install "Django>=5.0,<6.0"
```

**3) `sqlite3.OperationalError` or migration issues**  
Delete the local DB and re‑migrate (this removes your data):
```bash
# Stop the server first
# Then:
rm -f db.sqlite3  # use 'del db.sqlite3' on Windows
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**4) Static files not loading**  
Make sure `DEBUG = True` in `settings.py` for local dev, and avoid using `collectstatic` unless you configure static hosting.

**5) Port already in use**  
Use another port:
```bash
python manage.py runserver 8001
```

---

## 🙌 Credits

Built for learning purposes by the project author.  
Feel free to open issues or PRs to improve it!

---

## 📄 License

This is a student project. Choose a license you prefer (MIT is a good default) and add `LICENSE` to the repo.
