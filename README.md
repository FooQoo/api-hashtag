## Hashtag Capture

### Django rest framework
django-admin startproject your_project
cd your_project/
python manage.py startapp module

gunicorn --bind 127.0.0.1:8000 config.wsgi:application