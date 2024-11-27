# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]