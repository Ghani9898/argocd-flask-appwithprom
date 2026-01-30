# Use official Python image
FROM python:3.11-slim@sha256:89abad2fb0c3633705054018ae09caae4bd0e0febf57fb57a96fd41769c94e12


# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
