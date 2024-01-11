#!/bin/bash
set -e
#!/bin/bash
while true; do
  socat TCP-LISTEN:1337,reuseaddr,fork EXEC:'/chal/s',stderr
  sleep 1
done
