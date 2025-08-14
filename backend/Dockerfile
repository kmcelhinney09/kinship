# Start with a specific Python version for a consistent environment.
FROM python:3.11-slim-buster

# Set environment variables to prevent Python from writing .pyc files
# and to ensure output is sent straight to the terminal without buffering.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory for the application.
WORKDIR /app

# Install system dependencies required for psycopg2 (PostgreSQL adapter).
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Copy the requirements file first to leverage Docker's layer caching.
# The pip install command will only be re-run if this file changes.
COPY requirements.txt .

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user to run the application for better security.
RUN useradd -ms /bin/bash vscode
USER vscode

# Copy the rest of the application code into the container.
COPY . .

# The command to run the application will be specified in docker-compose.yml
