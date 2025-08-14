# Use a specific Node.js version. Alpine images are smaller.
FROM node:18-alpine

# Set the working directory inside the container.
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to leverage caching.
COPY package*.json ./

# Install project dependencies.
RUN npm install

# Copy the rest of the application source code.
COPY . .

# Expose the port the React app runs on.
EXPOSE 3000

# The command to start the app will be specified in docker-compose.yml
