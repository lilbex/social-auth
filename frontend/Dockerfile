# Use a node.js runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Build the React app
RUN npm run build

# Expose port 3000 to the outside world
EXPOSE 3000

# Run the React app
CMD ["npm", "start"]
