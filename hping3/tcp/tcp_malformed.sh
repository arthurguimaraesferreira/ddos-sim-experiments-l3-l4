sudo hping3 -S 192.168.100.2 -p 50001 -w 8192 --rand-source --flood -O 2 -b -d 13
sudo hping3 -S 192.168.100.2 -s 0 -p 0 --flood
sudo hping3 -S 192.168.100.2 -p 50001 -w 0 -O 2 --flood
sudo hping3 -S 192.168.100.2 -p 50001 -O 0 -d 0 -c 1

sudo hping3 192.168.100.2 -S -p 50001 -O 15 -d 0 -c 100 -b