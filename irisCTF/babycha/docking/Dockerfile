FROM ubuntu:latest as chroot

RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install pycryptodome
RUN /usr/sbin/useradd --no-create-home -u 1000 user

COPY chal.py /home/user/

FROM gcr.io/kctf-docker/challenge@sha256:0f7d757bcda470c3bbc063606335b915e03795d72ba1d8fdb6f0f9ff3757364f

COPY --from=chroot / /chroot

COPY nsjail.cfg /home/user/

CMD kctf_setup && \
    kctf_drop_privs \
    socat \
      TCP-LISTEN:1337,reuseaddr,fork \
      EXEC:"kctf_pow nsjail --config /home/user/nsjail.cfg -- /usr/bin/python3 /home/user/chal.py"