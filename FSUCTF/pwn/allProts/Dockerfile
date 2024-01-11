FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat

COPY ./s /chal/s
COPY ./flag.txt /chal/flag.txt
COPY ./start.sh /chal/start.sh
EXPOSE 1337

ENTRYPOINT ["/chal/start.sh" ]