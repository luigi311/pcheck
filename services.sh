#! /bin/bash

if [ ! -f /etc/ssl/private/key.key ]
then
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
            -keyout /etc/ssl/private/key.key -out /etc/ssl/certs/cert.crt \
            -subj "/C=US/ST=State/L=Locality/O=Organization/CN=Common"
fi

cd /pcheck
python manage.py makemigrations
python manage.py migrate
service nginx start
uwsgi --socket 0.0.0.0:8001 --chdir /pcheck/ --wsgi-file pcheck/wsgi.py --chmod-socket=664 --enable-threads
