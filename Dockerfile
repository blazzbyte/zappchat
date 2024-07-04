# Use the official Python 3.11 slim-buster image as the base
FROM python:3.11-slim-buster

# Metadata for maintainability 
LABEL maintainer="Blazzbyte <blazzmo.company@gmail.com>"
LABEL description="Dockerfile for ZappChat Project"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for building Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git

# Set the working directory within the container
WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Copy only the necessary files for Poetry to install dependencies
COPY pyproject.toml poetry.lock ./

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-root

# Copy the rest of the application code
COPY . .

# Expose the port your FastAPI application listens on
EXPOSE 8000

# Command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]