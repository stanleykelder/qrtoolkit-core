release: python manage.py migrate
web: gunicorn myqrtoolkit.wsgi
heroku ps:scale web=1