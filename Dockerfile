FROM python:2.7.11-alpine

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY . /src

CMD python manage.py runserver
