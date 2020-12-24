FROM ubuntu:bionic
LABEL maintainer = "Salvador HM <salvadorhm@gmail.com>"
LABEL description = "Ubuntu 18.04 with https://fastapi.tiangolo.com/"
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends sqlite3
RUN apt-get clean

EXPOSE 8000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir fastapi
RUN pip3 install --no-cache-dir uvicorn
RUN pip3 install --no-cache-dir sqlalchemy
RUN pip3 install --no-cache-dir mysql-connector-python
RUN pip3 install --no-cache-dir bcrypt
RUN pip3 install --no-cache-dir async-exit-stack async-generator

#RUN pip3 cache purge
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get remove -y python3-pip
