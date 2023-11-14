FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

# install dependancies
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt install -y git-all 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade -r requirements.txt

COPY . /app/

EXPOSE 3100

ENTRYPOINT [ "python3" ]

CMD ["app.py"]