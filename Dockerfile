FROM python:3.10-slim
WORKDIR /app
COPY monitor.py .
CMD ["python", "monitor.py"]