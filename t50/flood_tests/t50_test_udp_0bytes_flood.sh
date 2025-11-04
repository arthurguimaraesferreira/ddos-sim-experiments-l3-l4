#!/bin/bash

# T50 UDP Flood (0 bytes) (60 seconds)
sudo timeout 60 t50 192.168.100.2 --flood --protocol udp --dport 50001