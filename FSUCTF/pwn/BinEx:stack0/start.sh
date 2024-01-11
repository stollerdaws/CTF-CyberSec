#!/bin/bash

while true; do
  socat TCP-LISTEN:7331,reuseaddr,fork EXEC:'/stack0,pty,raw,echo=0',stderr
  sleep 1
done
