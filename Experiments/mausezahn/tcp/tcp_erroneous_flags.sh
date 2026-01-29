# TCP Erroneous Flags (command)
sudo mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "dp=50001,flags=syn+fin+psh+urg+rst+ack" -c 0