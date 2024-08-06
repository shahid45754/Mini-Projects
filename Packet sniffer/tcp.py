from scapy.all import sniff, IP, TCP

def packet_handler_tcp(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        print(f"Source IP: {packet[IP].src} -> Destination IP: {packet[IP].dst}")
        print(f"Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}")
        packet.show()


