FROM ubuntu:bionic
LABEL maintainer = "Salvador HM <salvadorhm@gmail.com>"
LABEL description = "Ubuntu 18.04 with fastapi config"
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y sqlite3
RUN apt-get clean

RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install sqlalchemy
RUN pip3 install mysql-connector-python
RUN pip3 install bcrypt
