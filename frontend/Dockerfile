# frontend/Dockerfile
# Dockerfile for the React frontend service.

# Use official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies first for better caching
COPY package.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Expose React dev server port
EXPOSE 3000
