# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements and install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy your Python script
COPY app.py .

# Run the script
ENTRYPOINT  ["python", "app.py"]
CMD []
