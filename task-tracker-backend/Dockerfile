# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV PORT 8080
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy requirements file and then install deps
COPY requirements.txt ./
RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev \
    && pip3 install -r requirements.txt --no-cache-dir

# Copy all other source code after installing reqs (so source code changes don't trigger re-installation)
COPY . ./
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.server.app:app