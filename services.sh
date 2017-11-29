#! /bin/bash

if [ ! -f /pcheck/static/cpu.json ];
then
    echo "Generating components"
    cd /
    git clone https://github.com/luigi311/PcPartPicker-API.git
    cd PcPartPicker-API
    pip install -r requirements.txt
    python components.py
    chmod 755 combine_cpu.sh
    ./combine_cpu.sh
    mv *.json /pcheck/static/
    cd /pcheck
    python manage.py generate --all
    python manage.py makemigrations
    python manage.py migrate
else
    echo "Components exist"
fi

service nginx start
uwsgi --socket 0.0.0.0:8001 --chdir /pcheck/ --wsgi-file pcheck/wsgi.py --chmod-socket=664 --enable-threads
