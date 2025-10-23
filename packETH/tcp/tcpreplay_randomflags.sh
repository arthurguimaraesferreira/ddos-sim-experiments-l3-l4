sudo tcpreplay -i enp0s3 -t tcp_random_flags.pcap
sudo tcpreplay -i enp0s3 -t -l 0 tcp_random_flags.pcap
