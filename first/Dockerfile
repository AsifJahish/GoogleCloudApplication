# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Define environment variable for the port
ENV PORT 8080

# Command to run the app with Gunicorn, bind to dynamic port
CMD ["gunicorn", "-b", ":$PORT", "app:app"]
