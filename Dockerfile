FROM python:slim

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y iputils-ping

COPY req.txt /app/
RUN pip install --no-cache-dir -r req.txt

COPY ./interview_task /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
