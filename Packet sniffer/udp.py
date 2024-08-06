from scapy.all import sniff, IP, UDP

def packet_handler_udp(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        print(f"Source IP: {packet[IP].src} -> Destination IP: {packet[IP].dst}")
        print(f"Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}")
        packet.show()


