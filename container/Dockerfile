# Use the official Node.js image from Docker Hub
FROM node:14

# Create a directory for the app
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose the application on port 3000
EXPOSE 3000

# Start the application
CMD ["node", "index.js"]
