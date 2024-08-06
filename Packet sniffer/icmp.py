from scapy.all import ICMP,sniff,IP

def packet_handler_icmp(packet):
    if packet.haslayer(IP) and packet.haslayer(ICMP):
        print(f"Source IP: {packet[IP].src} -> Destination IP: {packet[IP].dst}")
        packet.show()

