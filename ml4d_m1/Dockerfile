FROM ubuntu:18.04
LABEL maintainer = "Salvador HM <salvadorhm@gmail.com>"
LABEL description = "ML4D Community Edition"
LABEL version = 0.79

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN pip3 install -U pip
RUN pip3 install Cython
RUN pip3 install numpy --compile --pre
# Definbe ENV files
ENV requirements /home/requirements.txt

# Copy requirements file
COPY requirements.txt ${requirements}

# Install python packages
#RUN pip3 install numpy

RUN pip3 install -r /home/requirements.txt

RUN rm -rf /var/lib/apt/lists/*
