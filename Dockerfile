# set base image (host OS)
FROM python:3.7

ARG DISCORD_TOKEN_PARAMETER

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

ENV DISCORD_TOKEN=${DISCORD_TOKEN_PARAMETER}
ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 hunt_bot:app
