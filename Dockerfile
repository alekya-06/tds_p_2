# Dockerfile
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Set the PYTHONPATH to include the current directory
ENV PYTHONPATH=/app

# Copy the requirements file.
# Install the required packages
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000
EXPOSE 8001

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]


