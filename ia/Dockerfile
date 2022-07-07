FROM ubuntu:20.10

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY ./v3 /app
RUN pip3 install --upgrade pip && \
    pip3 install -r /app/requirements.txt

EXPOSE 5000
