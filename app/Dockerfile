FROM ubuntu:18.04

LABEL maintainer="Jonathan Peritz <jperitz@ufl.edu>"

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
