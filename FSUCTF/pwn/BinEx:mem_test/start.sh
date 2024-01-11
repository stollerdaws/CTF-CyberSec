#!/bin/bash

while true; do
  socat TCP-LISTEN:2425,reuseaddr,fork EXEC:'/mem_test,pty,raw,echo=0',stderr
  sleep 1
done
