from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"

# Flags comuns isoladas e combinadas
TCP_FLAGS_LIST = [
    'S',    # SYN
    'A',    # ACK
    'F',    # FIN
    'R',    # RST
    'P',    # PSH
    'U',    # URG
    'SA',   # SYN+ACK
    'FA',   # FIN+ACK
    'PA',   # PSH+ACK
    'RA',   # RST+ACK
    'FPA',  # FIN+PSH+ACK
]

PCAP_FILENAME = "tcp_random_flags_small.pcap"

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_flood_attack():
    bot_ips = load_bots(BOTFILE)
    numero_de_pacotes_enviados = 0
    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        flags = random.choice(TCP_FLAGS_LIST)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags=flags, seq=seq_num, window=8192)

        packet = eth_layer / ip_layer / tcp_layer 
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == 100:
            break

    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")

if __name__ == "__main__":
    run_tcp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 create-pcap-random-flags.py