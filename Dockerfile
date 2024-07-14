FROM alpine:3.19

# Update package index and install putils-ping
RUN apk update && \
    apk add iputils-ping python3 py3-pip

COPY req.txt .
RUN pip3 install -r req.txt --break-system-packages

WORKDIR /app

COPY interview_task /app
RUN ls -la .
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]