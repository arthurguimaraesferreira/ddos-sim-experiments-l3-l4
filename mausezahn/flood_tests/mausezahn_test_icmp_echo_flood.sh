#!/bin/bash

# Mausezahn ICMP Echo Flood (60 seconds)
sudo timeout -s INT 60 mausezahn enp0s3 -A rand -B 192.168.100.2 -t icmp "type=8,code=0" -c 0