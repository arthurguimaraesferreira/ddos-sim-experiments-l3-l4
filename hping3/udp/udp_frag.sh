# Real Frag
sudo hping3 -2 192.168.100.2 -p 50001 --rand-source -d 2000 -c 10 -f

# Fake Frag (Not Working)
sudo hping3 -2 192.168.100.2 -p 50001 --rand-source -d 20 -x -g 40 -c 100 --flood 