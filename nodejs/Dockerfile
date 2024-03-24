# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Node.js app
CMD ["node", "index.js"]
