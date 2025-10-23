from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
BOTFILE = "bots.txt"

PCAP_FILENAME = "icmp_frag.pcap"

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

    # Define um payload grande para forçar a fragmentação (por exemplo, 4000 bytes)
    icmp_payload = b"A" * 4000

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0) / icmp_payload  # Echo Request com payload grande
        packet = ip_layer / icmp_layer
        # Fragmenta o pacote IP (isso retorna uma lista de fragmentos)
        fragments = fragment(packet, fragsize=1480)  # MTU típica menos cabeçalhos
        for frag in fragments:
            lista_de_pacotes.append(eth_layer / frag)
            numero_de_pacotes_enviados += 1
            if numero_de_pacotes_enviados == 100:
                break
        if numero_de_pacotes_enviados == 100:
            break

    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")

if __name__ == "__main__":
    run_icmp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 create-icmp-frag.py