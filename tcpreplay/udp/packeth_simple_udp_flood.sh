sudo ./packETHcli -i enp0s3 -m 6 -n 35000 -L "35000 0 0" -f packeth_simple_udp_flood.pcap
sudo ./packETHcli -i enp0s3 -m 6 -n 0 -L "35000 0 0" -f packeth_simple_udp_flood.pcap

RANDOMRATE: sudo tcpreplay -i enp0s3 --timer=gtod udp_flood_random_rate.pcap
