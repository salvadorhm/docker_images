FROM ubuntu:bionic
LABEL maintainer = "Salvador HM <salvadorhm@gmail.com>"
LABEL description = "ML4D Community Edition"
LABEL version = 0.79

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y python3-pip
RUN apt-get clean

# Definbe ENV files
ENV requirements /home/requirements.txt

# Copy requirements file
COPY requirements.txt ${requirements}

# Install python packages
RUN pip3 install --no-cache-dir -r /home/requirements.txt

RUN rm -rf /var/lib/apt/lists/*
