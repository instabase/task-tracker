# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /workspace
WORKDIR $APP_HOME

# Copy requirements file and then install deps
COPY requirements.txt ./
RUN apt-get update -y \
    && apt-get install -y gcc libpq-dev firefox-esr \
    && pip3 install -r requirements.txt --no-cache-dir \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz \
    && tar -xvf geckodriver-v0.29.1-linux64.tar.gz \
    && mv geckodriver /usr/bin/geckodriver \
    && chown root:root /usr/bin/geckodriver \
    && chmod +x /usr/bin/geckodriver \
    && python -m playwright install

# Copy all other source code after installing reqs (so source code changes don't trigger re-installation)
COPY . ./
