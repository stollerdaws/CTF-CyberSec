#!/bin/bash
set -e
#!/bin/bash
while true; do
  socat TCP-LISTEN:1886,reuseaddr,fork EXEC:'/chall',stderr
  sleep 1
done
