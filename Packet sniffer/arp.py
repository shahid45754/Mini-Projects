from scapy.all import sniff, ARP

def packet_handler_arp(packet):
    if packet.haslayer(ARP):
        print(f"ARP Request: {packet[ARP].psrc} is asking about {packet[ARP].pdst}")
        packet.show()


