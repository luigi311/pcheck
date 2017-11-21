# Build the docker image with
# "docker build -t <name for image> ."
# Access shell 
# "docker run -it <name for image> bash"

# Image source for the docker image. ubuntu/fedora/nginx/apache
FROM nginx


# Pass through specific port from docker image onto the actual computer for Https/SSL 
EXPOSE 443
# Map exposed port to a different port on the machine from command line with
# "docker run -p <different port>:443 <image name>"


# Run commands when building the docker image
# Install openssl package in order to create ssl certificates, gnupg to import repository keys, python-pip for installing django
RUN apt-get update 
RUN apt-get install -y \
    openssl \
    python-pip  
RUN pip install django
RUN pip install uwsgi

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/key.key -out /etc/ssl/certs/cert.crt \
    -subj "/C=US/ST=State/L=Locality/O=Organization/CN=Common"


# Setup Django project
RUN django-admin startproject pcheck


#Copy over the django configuration file
COPY uwsgi_params /pcheck/uwsgi_params

RUN cd /pcheck && python manage.py startapp compatability
COPY django/pcheck/settings.py /pcheck/pcheck/settings.py
RUN cd /pcheck && python manage.py collectstatic

COPY django/compatability/ /pcheck/compatability/
COPY django/static/ /pcheck/static/

RUN cd /pcheck && python manage.py makemigrations
RUN cd /pcheck && python manage.py migrate

RUN cd /pcheck && python manage.py generate

RUN cd /pcheck && python manage.py makemigrations
RUN cd /pcheck && python manage.py migrate


# Create the folder to hold the enabled websites
RUN mkdir -p /etc/nginx/sites-enabled

# Copy files over from the computer onto the docker image
# Copy the nginx configuration file and replace the default one
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the configuration for the website
COPY default /etc/nginx/sites-enabled/default

# Copy over the run.sh script that will start the services and keep docker running
COPY services.sh /services.sh
RUN chmod 755 /services.sh


# Run everything
CMD /services.sh