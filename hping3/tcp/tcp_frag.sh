# Real Frag
sudo hping3 -S 192.168.100.2 -p 50001 -w 8192 --rand-source -d 2000 -f -c 20

# Fake Frag (Not Working) 
sudo hping3 -S 192.168.100.2 -p 50001 -w 8192 --rand-source -d 20 -x -g 80 -c 20