 FROM python:3
 ENV VER=1
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 WORKDIR /app
 ADD ./src/ /app/
 RUN chown root:root -R *
 RUN pip install -r requirements.txt
 RUN ./manage.py collectstatic --noinput
