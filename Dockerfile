# Start with a Python 3.10 base image
FROM python:3.10-slim

# Set environment variables to ensure non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for Poetry and your Python dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry (using the recommended installation method)
RUN curl -sSL https://install.python-poetry.org | python3 -

# Ensure poetry is available globally
ENV PATH="/root/.local/bin:${PATH}"

# Set the working directory
WORKDIR /app

# Copy the Poetry configuration files (pyproject.toml and poetry.lock)
COPY pyproject.toml poetry.lock* ./

# Install the dependencies using Poetry
RUN poetry install --no-root --no-dev

# Copy the rest of the application files (excluding files specified in .dockerignore)
COPY . .

# Set the entrypoint or command to run the application (assuming main.py is the entry point)
CMD ["poetry", "run", "python", "streamlit-app/app.py"]
