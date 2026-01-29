# UDP Custom Payload (command)
sudo hping3 -2 192.168.100.2 -p 50001 --rand-source -E payload.bin -d 15 -c 10