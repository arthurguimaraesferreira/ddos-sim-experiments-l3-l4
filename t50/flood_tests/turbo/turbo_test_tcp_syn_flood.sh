#!/bin/bash

# T50 TCP SYN Flood (60 seconds)
sudo timeout -s INT 60 t50 192.168.100.2 --flood --turbo --protocol tcp --dport 50001 --syn --window 8192
# Window = 8192 not working