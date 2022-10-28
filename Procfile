web: gunicorn Portfolio.wsgi:application --log-file - --log-level debug
python Portfolio/manage.py collectstatic --noinput
manage.py migrate