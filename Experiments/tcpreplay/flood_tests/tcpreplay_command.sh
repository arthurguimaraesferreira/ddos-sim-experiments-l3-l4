# Comando para acionar as simulações de flood com Tcpreplay (60 seconds)
# -t = topspeed
sudo timeout -s INT 60 tcpreplay -i <interface> -t -K -l 0 <file>.pcap