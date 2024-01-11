FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat

COPY ./picker-IV /picker-IV
COPY ./flag.txt /flag.txt
COPY ./start.sh /start.sh
EXPOSE 4444

ENTRYPOINT ["/start.sh" ]