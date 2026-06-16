FROM python:3.13.7-slim

# Install system dependencies for headless GUI applications
# Upgrade openssl to patch CVE-2026-31789, CVE-2026-28388, CVE-2026-28390
RUN apt-get update && apt-get install -y --no-install-recommends \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpango-1.0-0 \
    libx11-xcb1 \
    libxcursor1 \
    libxfixes3 \
    libxrender1 \
    libxtst6 \
    openssl \
    && apt-get upgrade -y openssl \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONPATH=/app/src

# Set the working directory
WORKDIR /app

# Copy and install dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt

# Copy the entire source code
COPY ./src /app/src

# Create non-root user and switch to it
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Set the entry point to your main script
ENTRYPOINT ["python", "-m", "pystarter"]
