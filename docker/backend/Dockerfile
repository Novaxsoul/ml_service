FROM ubuntu:jammy

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3-pip

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.10 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.10 /usr/bin/python3

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn==23.0.0

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

RUN mkdir -p /app/backend/server/static
