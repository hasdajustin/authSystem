
# 🔐 Django Authentication System
This is a simple Django project that implements user authentication, including:
- User Registration
- User Login & Logout
- Home Page (Login Required)
- Flash Messages using Django's `messages` framework
## 🛠 Features
- Django 5.2+
- Secure Login & Logout
- Registration with password validation
- Flash messages for feedback (success, error)
- Login required for home page access
- Bootstrap 5 for UI

---

## 📁 Project Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/hasdajustin/authSystem.git
```
```bash
cd django-auth-system
```
### Create and Activate Virtual Environment
```bash
python -m venv env
```
- Windows
```bash
env\Scripts\activate
```
- Linux / macOS
```bash
source env/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run Migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
### Run the Development Server
```bash
python manage.py runserver
```
- Visit: http://127.0.0.1:8000
