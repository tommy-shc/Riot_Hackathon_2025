# Use Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the app
CMD ["python", "main.py"]