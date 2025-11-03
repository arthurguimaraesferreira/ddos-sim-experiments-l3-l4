#!/bin/bash

INTERFACE="enp0s3"
FILTER="icmp and icmp.type == 8 and ip.dst == 192.168.100.2"
TMPFILE="icmp_capture.txt"
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

# Wait 3 seconds to ensure file is fully written
sleep 3

# Analyze captured data using calculator.sh
if [ -s "$TMPFILE" ]; then
    ./calculator.sh "$TMPFILE"
else
    echo "No packets captured."
fi