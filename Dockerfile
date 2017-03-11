FROM ubuntu:14.04

RUN sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt-get update 
RUN apt-get install -y \ 
    build-essential \
    libmysqlclient-dev \
    python-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    zlib1g-dev \
    python-pip 

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . /src


RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('${SUPER_USER:-admin}', '', '${SUPER_PASSWORD:-athena}')" | python manage.py shell >> /dev/null
CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
