# TCP SYN (command)
# Window = 8192 not working
sudo t50 192.168.100.2 --flood --protocol tcp --dport 50001 --syn --window 8192