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

CMD ["python", "./hunt_bot.py"]