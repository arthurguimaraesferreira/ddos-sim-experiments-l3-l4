from scapy.all import *
import random
import time
import ipaddress

# TCP Erroneous Flags
TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "../bots.txt"
NUM_PACKETS = 100

INVALID_TCP_FLAGS_LIST = [
    'SF',      # SYN + FIN
    'SR',      # SYN + RST
    'SFR',     # SYN + FIN + RST
    'SFP',     # SYN + FIN + PSH
    'FR',      # FIN + RST
    'SFRP',    # SYN + FIN + RST + PSH
    'FSRPAU',  # All
    'FPU',     # FIN + PSH + URG
    'FPAU',    # FIN + PSH + ACK + URG
    'FSA',     # FIN + SYN + ACK
    'FSAU',    # FIN + SYN + ACK + URG
]

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_erroneous_flags_attack():
    bot_ips = load_bots(BOTFILE)
    numero_de_pacotes_enviados = 0
    lista_de_pacotes = []

    while True:
        source_ip = random.choice(bot_ips)
        ip_layer = IP(src=source_ip, dst=TARGET_IP)
        eth_layer = Ether()
        seq_num = random.randint(0, 4294967295)
        flags = random.choice(INVALID_TCP_FLAGS_LIST)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags=flags, seq=seq_num, window=8192)

        packet = eth_layer / ip_layer / tcp_layer 
        lista_de_pacotes.append(packet)
        numero_de_pacotes_enviados += 1

        if numero_de_pacotes_enviados == NUM_PACKETS:
            break

    start_time = time.perf_counter()
    wrpcap("tcp_erroneous_flags.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_tcp_erroneous_flags_attack()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 tcp_erroneous_flags.py