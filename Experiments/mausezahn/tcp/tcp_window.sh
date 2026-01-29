# TCP Window 0 (command)
sudo mausezahn enp0s3 -A rand -B 192.168.100.2 -t tcp "sp=80, dp=50001, flags=syn, win=0" -c 0