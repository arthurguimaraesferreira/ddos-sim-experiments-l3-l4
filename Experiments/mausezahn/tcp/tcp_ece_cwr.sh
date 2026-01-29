# TCP ECE (command)
sudo mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "dp=50001,flags=ecn" -c 0

# TCP CWR (command)
sudo mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "dp=50001,flags=cwr" -c 0