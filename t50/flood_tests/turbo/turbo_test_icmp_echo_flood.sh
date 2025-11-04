#!/bin/bash

# T50 ICMP Echo Flood (60 seconds)
sudo timeout -s INT 60 t50 192.168.100.2 --protocol icmp --flood --turbo --ttl 64