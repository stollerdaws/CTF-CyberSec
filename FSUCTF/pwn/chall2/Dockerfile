FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    socat \
 && rm -rf /var/lib/apt/lists/*

COPY vuln /vuln
COPY flag.txt /flag.txt

RUN chmod +x /vuln

EXPOSE 1118

CMD ["socat", "TCP-LISTEN:1118,reuseaddr,fork", "EXEC:/vuln,stderr"]