# Django Online Quiz Application

## Features
- User registration & login (Django auth)
- Admin can create quizzes, questions, and choices
- Timed quiz attempt with auto-submit
- Auto scoring and result page
- Leaderboard for top scorers
- Bootstrap UI

## Setup (local)
1. Create virtual env and activate it:
   - `python -m venv venv`
   - `source venv/bin/activate` (Linux/mac) or `.env\Scripts\Activate.ps1` (Windows PowerShell)

2. Install requirements:
   - `pip install -r requirements.txt`

3. Run migrations and create superuser:
   - `python manage.py migrate`
   - `python manage.py createsuperuser`

4. Run server:
   - `python manage.py runserver`
   - Open http://127.0.0.1:8000/

## Admin
- Access /admin to create quizzes, questions, and choices.

## Notes
- SECRET_KEY in settings.py should be changed for production.
- DEBUG is True for development.
