FROM python:3.13.1-slim

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Update and install required dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libssl-dev \
        libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s "$POETRY_HOME/bin/poetry" /usr/local/bin/poetry

# Set the working directory
WORKDIR /app

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Specify the entry point (update as needed for your application)
CMD ["poetry", "run", "python", "./main.py"]