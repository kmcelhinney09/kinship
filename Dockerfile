FROM node:22-bullseye

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install uv

WORKDIR /app

# COPY command (already correct)
COPY ./backend/requirements.txt ./backend/

# Update the RUN command with --system
RUN uv pip install --system --no-cache-dir -r ./backend/requirements.txt

# Set the working directory for the frontend application
WORKDIR /app/frontend

# Copy package.json and tsconfig.json to the container
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
COPY ./frontend/tsconfig.json ./
COPY ./frontend/tsconfig.node.json ./

# Install npm dependencies
RUN npm install

EXPOSE 3000
EXPOSE 8000

CMD ["tail", "-f", "/dev/null"]