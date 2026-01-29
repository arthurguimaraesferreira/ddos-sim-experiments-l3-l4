# TCP Xmas (command)
sudo mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "dp=50001,flags=fin+urg+psh" -c 0