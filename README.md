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

<img width="1920" height="1080" alt="Screenshot (75)" src="https://github.com/user-attachments/assets/0d1a51c2-2228-4e65-9a4b-9c033105b491" />



<img width="1920" height="1080" alt="Screenshot (76)" src="https://github.com/user-attachments/assets/c5bab758-d1a5-4ce7-b358-c81edd707998" />
<img width="1920" height="1080" alt="Screenshot (77)" src="https://github.com/user-attachments/assets/0d5fd709-0de7-4fc4-bfd2-0648ed7a65eb" /><img width="1920" height="1080" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/8aac65a1-4595-43f6-a8af-8a87a840829e" />


