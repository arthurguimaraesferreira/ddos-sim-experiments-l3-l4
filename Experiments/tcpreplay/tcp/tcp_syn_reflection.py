from scapy.all import *
import time
import random

# TCP SYN Reflection
VICTIM_IP = "192.168.100.2"
REFLECTOR_IP = "192.168.100.3"
TARGET_PORT = 50001
NUM_PACKETS = 100

def run_tcp_syn_reflection():
    
    lista_de_pacotes = []
    for i in range(NUM_PACKETS):
        ip_layer = IP(src=VICTIM_IP, dst=REFLECTOR_IP)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S')
        packet = Ether() / ip_layer / tcp_layer
        lista_de_pacotes.append(packet)

    start_time = time.perf_counter()
    wrpcap("tcp_syn_reflection.pcap", lista_de_pacotes)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_tcp_syn_reflection()

# Comando: sudo PYTHONPATH=$HOME/scapy python3 tcp_syn_reflection.py