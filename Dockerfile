FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y iputils-ping python3 python3-pip


RUN pip3 install django

WORKDIR /app

COPY ./interview_task /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
