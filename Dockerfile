# Base image
FROM python:3.11-slim

# Set working Directory
WORKDIR /app

# Copy requirements file to the container
COPY requirement.txt .

# Install Dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirement.txt

# Default entrypoint
#ENTRYPOINT ["pytest"]