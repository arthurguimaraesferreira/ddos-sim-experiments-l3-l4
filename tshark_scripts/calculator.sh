#!/bin/bash

# Usage: ./calculator.sh timestamps_file.txt

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
fi

# Count number of packets (lines with a valid timestamp)
count=$(grep -E '^[0-9]+\.[0-9]+$' "$FILE" | wc -l)

# Get the first and last valid timestamp
first=$(grep -E '^[0-9]+\.[0-9]+$' "$FILE" | head -n 1)
last=$(grep -E '^[0-9]+\.[0-9]+$' "$FILE" | tail -n 1)

if [[ -z "$first" || -z "$last" ]]; then
    echo "No valid timestamps found in $FILE."
    exit 1
fi

# Calculate duration (in seconds)
duration=$(echo "$last - $first" | bc -l)

echo "Packets captured: $count"
echo "Timestamp of the first packet: $first"
echo "Timestamp of the last packet: $last"
echo "Duration (seconds): $duration"