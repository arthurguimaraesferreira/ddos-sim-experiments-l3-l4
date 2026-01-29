# TCP SACK (commands)
sudo t50 192.168.100.2 --protocol tcp --ack --psh --sack 40000:42000 --dport 50001 --threshold 100
sudo t50 192.168.100.2 --protocol tcp --ack --sack-ok --sack 15000:15500 --dport 50001 --threshold 100