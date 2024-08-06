from scapy.all import sniff, get_if_list
from tcp import packet_handler_tcp
from udp import packet_handler_udp
from arp import packet_handler_arp
from icmp import packet_handler_icmp
from art import *


print_sniffer_art()
print("Welcome to Sniffing Dog!")
jack = True

while jack:
    User = input("What protocol do you want to sniff (ARP,icmp,TCP, UDP)? If you want to exit, type 'exit': ").lower()
    
    
    if User == "tcp":
        sniff(prn=packet_handler_tcp, filter="tcp", count=3)
    elif User == "icmp":
        sniff(prn=packet_handler_icmp,filter="icmp",count=3)
    elif User == "arp":
        sniff(prn=packet_handler_arp, filter="arp", count=3)
    elif User == "udp":
        sniff(prn=packet_handler_udp, filter="udp", count=3)
    elif User == "exit":
        print("Thank You!")
        jack = False
        continue
    else:
        print("Invalid input. Please try again.")
    
    if jack:
        Choice = input("Do you want to continue? Type 'yes' or 'no': ").lower()
        if Choice == "no":
            print("Thank You!")
            jack = False
