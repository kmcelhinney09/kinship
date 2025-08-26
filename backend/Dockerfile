# backend/Dockerfile
# Dockerfile for the Django REST API backend service.

# Use official Python image
FROM python:3.11-slim-bookworm

# Set working directory
WORKDIR /app

# Install system dependencies for building Python packages and PostgreSQL support
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for VS Code with specific UID and GID
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g ${GROUP_ID} vscode \
    && useradd -m -s /bin/bash -u ${USER_ID} -g ${GROUP_ID} vscode \
    && mkdir -p /app \
    && chown vscode:vscode /app
USER vscode

# Copy the rest of the backend code
COPY --chown=vscode:vscode . .
