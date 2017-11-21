#! /bin/bash
cd /pcheck && python manage.py createsuperuser
service nginx start
uwsgi --socket 0.0.0.0:8001 --chdir /pcheck/ --wsgi-file pcheck/wsgi.py --chmod-socket=664 --enable-threads
