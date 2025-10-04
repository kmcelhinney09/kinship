# Devcontainer base: Debian Bullseye with Python 3.13
FROM python:3.13-slim-bullseye

# Avoid interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates git build-essential \
    libpq-dev sudo \
    && rm -rf /var/lib/apt/lists/*

# Node.js is provided via devcontainer Feature in devcontainer.json

# Create a non-root user (vscode) to match devcontainers convention
RUN useradd -m -s /bin/bash vscode \
    && mkdir -p /etc/sudoers.d \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-vscode \
    && chmod 0440 /etc/sudoers.d/90-vscode
USER vscode

# Ensure local bins are on PATH
ENV PATH=/home/vscode/.local/bin:$PATH

# Default workdir
WORKDIR /workspaces/kinship

# Keep container alive for VS Code attach
CMD ["sleep", "infinity"]
