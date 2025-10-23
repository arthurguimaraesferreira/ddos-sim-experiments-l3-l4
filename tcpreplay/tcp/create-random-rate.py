from scapy.all import Ether, IP, TCP, RandShort, PcapWriter
import random, ipaddress, time

# CONFIG
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
TARGET_MAC = "ff:ff:ff:ff:ff:ff"
PCAP_FILENAME = "tcp_syn_flood_random_rate.pcap"

# Intervalos (segundos) para espaçar pacotes de forma aleatória
MIN_DELAY = 0.001   # 1 ms
MAX_DELAY = 0.200   # 200 ms

def load_bots(filename):
    bots = []
    with open(filename) as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)  # valida
                bots.append(ip)
    return bots

def run_tcp_flood_attack():
    bots = load_bots(BOTFILE)
    writer = PcapWriter(PCAP_FILENAME, append=False, sync=True)

    now = time.time()
    for _ in range(35000):
        src_ip = random.choice(bots)
        pkt = (
            Ether(dst=TARGET_MAC) /
            IP(src=src_ip, dst=TARGET_IP) /
            TCP(sport=RandShort(), dport=TARGET_PORT, flags='S',
                seq=random.randint(0, 0xFFFFFFFF), window=8192)
        )
        # define o timestamp do pacote ANTES de escrever
        pkt.time = now
        writer.write(pkt)

        # incrementa tempo com atraso aleatório
        now += random.uniform(MIN_DELAY, MAX_DELAY)

    writer.close()
    print(f"Arquivo PCAP '{PCAP_FILENAME}' gerado com 35000 pacotes.")

if __name__ == "__main__":
    run_tcp_flood_attack()
