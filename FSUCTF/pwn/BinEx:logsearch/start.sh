#!/bin/bash

while true; do
  socat TCP-LISTEN:1993,reuseaddr,fork EXEC:'/logsearch,pty,raw,echo=0',stderr
  sleep 1
done
