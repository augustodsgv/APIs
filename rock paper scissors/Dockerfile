FROM ubuntu:latest

WORKDIR /home/server

COPY ./main.py .
COPY ./requirements.txt .

RUN apt update && apt upgrade -y
RUN apt install python3 -y
RUN apt install python3-pip -y

RUN pip3 install -r requirements.txt

CMD uvicorn --host=0.0.0.0 main:app

EXPOSE 8000