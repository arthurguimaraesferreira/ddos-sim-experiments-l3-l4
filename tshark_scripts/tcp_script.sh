#!/bin/bash

# Network interface to monitor
INTERFACE="enp0s3"
# BPF filter for TCP packets destined to the victim
FILTER="tcp and ip.dst == 192.168.100.2"
# Temporary file to store the capture
TMPFILE="tcp_capture.txt"
# Time in seconds to wait before stopping after inactivity
INACTIVITY=5

# Clear previous capture file
> "$TMPFILE"

# Start tshark capture in the background
sudo tshark -i "$INTERFACE" -Y "$FILTER" -T fields -e frame.time_epoch >> "$TMPFILE" &
TSHARK_PID=$!

echo "Capturing... Will auto-stop after $INACTIVITY seconds of inactivity."

LAST_LINES=0
while kill -0 $TSHARK_PID 2>/dev/null; do
    sleep $INACTIVITY
    NEW_LINES=$(wc -l < "$TMPFILE")
    if [ "$NEW_LINES" -eq "$LAST_LINES" ]; then
        echo "No new packets for $INACTIVITY seconds. Stopping capture."
        kill $TSHARK_PID
        break
    fi
    LAST_LINES=$NEW_LINES
done

# Analyze captured data
if [ -s "$TMPFILE" ]; then
    first=$(head -n 1 "$TMPFILE")
    last=$(tail -n 1 "$TMPFILE")
    count=$(wc -l < "$TMPFILE")
    duration=$(echo "$last - $first" | bc -l)

    echo "Packets captured: $count"
    echo "Timestamp of the first packet: $first"
    echo "Timestamp of the last packet: $last"
    echo "Duration (seconds): $duration"
else
    echo "No packets captured."
fi

