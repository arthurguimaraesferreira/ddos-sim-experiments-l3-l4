# TCP ECE
sudo hping3 -X 192.168.100.2 -p 50001 --rand-source --flood

# TCP CWR
sudo hping3 -Y 192.168.100.2 -p 50001 --rand-source --flood