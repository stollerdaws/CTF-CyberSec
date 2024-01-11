FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat

COPY ./chall /chall
COPY ./flag.txt /flag.txt
COPY ./start.sh /start.sh
EXPOSE 1886

ENTRYPOINT ["/start.sh" ]