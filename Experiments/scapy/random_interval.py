from scapy.all import *
import random
import time
import ipaddress

# Taxa de Envio Random
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
NUM_PACKETS = 1000

MIN_INTERVAL = 0.001  # 1 ms
MAX_INTERVAL = 1      # 1 s

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_random_interval():
    bot_ips = load_bots(BOTFILE)
    sent = 0
    start_time = time.perf_counter()
    while sent < NUM_PACKETS:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        udp_layer = UDP(sport=RandShort(), dport=TARGET_PORT)
        packet = eth_layer / ip_layer / udp_layer
        sendp(packet, iface="enp0s3", verbose=0)
        sent += 1
        interval = random.uniform(MIN_INTERVAL, MAX_INTERVAL)
        time.sleep(interval)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nSending completed.")
    print(f"Total time to send packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_random_interval()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 random_interval.py