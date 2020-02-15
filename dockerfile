FROM ubuntu:latest

LABEL Maintainer="Jack Owens - github.com/rjackowens"

WORKDIR .

RUN apt-get update -y
RUN apt-get install -y python3-pip python3.7

COPY . .

ARG SENDER_EMAIL
ARG RECEIVER_EMAIL
ARG EMAIL_PASSWORD

ENV SENDER_EMAIL=$SENDER_EMAIL
ENV RECEIVER_EMAIL=$RECEIVER_EMAIL
ENV EMAIL_PASSWORD=$EMAIL_PASSWORD

RUN export FLASK_APP=src/__init__.py

RUN pip3 install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org -r requirements.txt

CMD [ "python3", "main.py" ]
