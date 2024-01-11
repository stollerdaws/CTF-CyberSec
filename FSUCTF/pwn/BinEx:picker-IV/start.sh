#!/bin/bash
set -e
#!/bin/bash
while true; do
  socat TCP-LISTEN:4444,reuseaddr,fork EXEC:'/picker-IV',stderr
  sleep 1
done
