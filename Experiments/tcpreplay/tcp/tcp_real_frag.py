from scapy.all import *
import random
import time
import ipaddress
import os

# TCP Real Frag
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "../bots.txt"
NUM_PACKETS = 100
PACKET_PAYLOAD_SIZE = 4000  # Big payload
FRAGSIZE = 1480             # Typical MTU

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_real_frag():
    bot_ips = load_bots(BOTFILE)
    numero_de_pacotes_enviados = 0
    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192)
        payload = os.urandom(PACKET_PAYLOAD_SIZE)  # Random payload

        packet = ip_layer / tcp_layer / Raw(load=payload)

        # Frag
        fragments = fragment(packet, fragsize=FRAGSIZE)

        for frag in fragments:
            lista_de_pacotes.append(eth_layer / frag)
            numero_de_pacotes_enviados += 1
            if numero_de_pacotes_enviados == NUM_PACKETS:
                break
        if numero_de_pacotes_enviados == NUM_PACKETS:
            break

    start_time = time.perf_counter()
    wrpcap("tcp_real_frag.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_tcp_real_frag()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 tcp_real_frag.py