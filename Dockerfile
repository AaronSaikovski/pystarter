# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-buster

RUN pip install poetry==1.5.1

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
CMD ["python", "src/main.py"]