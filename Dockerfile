FROM python:3.13.2-slim



# Install system dependencies required by Playwright
RUN apt-get update && apt-get install -y \
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
    wget \
    libsqlite3-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

################################################
#Environment Variables
ENV SOME_VAR="abc123"
################################################

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy the entire source code
COPY ./src /app/src

# Set the entry point to your main script in the src folder
ENTRYPOINT ["python", "src/main.py"]


