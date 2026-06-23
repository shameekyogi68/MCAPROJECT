# Use an official Python slim image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 7860 (Hugging Face Spaces default)
EXPOSE 7860

# Define environment variables for the cloud run
ENV PORT=7860
ENV HOST=0.0.0.0

# Run the NiceGUI application
CMD ["python", "main.py"]
