FROM ubuntu:bionic
LABEL maintainer = "Salvador HM <salvadorhm@gmail.com>"
LABEL description = "Ubuntu 18.04 with https://fastapi.tiangolo.com/"
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y sqlite3
RUN apt-get clean

EXPOSE 8000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install sqlalchemy
RUN pip3 install mysql-connector-python
RUN pip3 install bcrypt
RUN pip3 install async-exit-stack async-generator

