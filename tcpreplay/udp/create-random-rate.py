from scapy.all import Ether, IP, UDP, RandShort, PcapWriter
import random
import ipaddress
import time

# CONFIGURAÇÃO DO ATAQUE
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
TARGET_MAC = "ff:ff:ff:ff:ff:ff"
PCAP_FILENAME = "udp_flood_random_rate.pcap"

# Defina os intervalos aleatórios entre pacotes (em segundos)
MIN_DELAY = 0.001   # 1 ms
MAX_DELAY = 2.0     # 200 ms

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
    bot_ips = load_bots(BOTFILE)
    writer = PcapWriter(PCAP_FILENAME, append=False, sync=True)
    now = time.time()
    for _ in range(5000):
        src_ip = random.choice(bot_ips)
        pkt = (
            Ether(dst=TARGET_MAC) /
            IP(src=src_ip, dst=TARGET_IP) /
            UDP(sport=RandShort(), dport=TARGET_PORT)
        )
        pkt.time = now
        writer.write(pkt)
        # Adiciona delay aleatório ao timestamp do próximo pacote
        now += random.uniform(MIN_DELAY, MAX_DELAY)
    writer.close()
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com 5000 pacotes (intervalos aleatórios).")

if __name__ == "__main__":
    run_udp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 create-random-rate.py