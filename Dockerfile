FROM python:3.9

WORKDIR /app

RUN pip install --no-cache-dir \
    Flask==2.0.2

COPY . .

CMD ["python", "webhook_server.py"]

