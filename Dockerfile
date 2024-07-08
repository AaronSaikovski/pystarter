# For more information, please refer to https://hub.docker.com/_/python
FROM python:3.12.4-slim-bookworm

run pip install --upgrade pip
RUN pip install poetry 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

#copy poetry files
COPY ./pyproject.toml ./
COPY ./poetry.lock ./

# Install poetry and project dependencies
RUN poetry install --without dev

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "./main.py"]