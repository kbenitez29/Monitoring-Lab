FROM mirror.gcr.io/library/python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir flask prometheus-flask-exporter
COPY . .
CMD ["python", "app.py"]
