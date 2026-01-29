from scapy.all import *
import scapy
import random
import time
import sys
import ipaddress

# UDP-TCP Custom Ports
TARGET_IP = "192.168.100.2"
BOTFILE = "bots.txt"
NUM_PACKETS = 100
PACKET_PAYLOAD_SIZE = 512

CUSTOM_SOURCE_PORT = 80 # RandShort() for random
CUSTOM_DEST_PORT = 0    # RandShort() for random

def load_bots(filename):
    bot_ips = []

    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)

    return bot_ips

def run_custom_ports():
    bot_ips = load_bots(BOTFILE)

    numero_de_pacotes_enviados = 0

    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)

        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        udp_layer = UDP(sport=CUSTOM_SOURCE_PORT, dport=CUSTOM_DEST_PORT)

        payload = b'*' * PACKET_PAYLOAD_SIZE

        packet = eth_layer / ip_layer / udp_layer / Raw(load=payload)

        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if(numero_de_pacotes_enviados == NUM_PACKETS):
            break


    start_time = time.perf_counter()
    wrpcap("udp-tcp_custom_ports.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")


if __name__ == "__main__":
    run_custom_ports()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 udp-tcp_custom_ports.py