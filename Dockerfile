# python-service/Dockerfile
FROM python:3.10-slim

# Create a working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# By default, let the docker-compose.yml 'command' override the final command.
