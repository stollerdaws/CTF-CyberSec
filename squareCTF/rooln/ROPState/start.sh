#!/bin/bash

while true; do
  socat TCP-LISTEN:1118,reuseaddr,fork EXEC:'/roplon,pty,raw,echo=0',stderr
  sleep 1
done
