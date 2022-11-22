from collections import defaultdict
import pyshark

ip_addr = defaultdict(int)

def packet_sniff(ip: str):

    syn = 2
    ack = 10

    capture = pyshark.LiveCapture(interface='eth0')

    try:
        for packet in capture.sniff_continuously():
            if "IP" in packet and "TCP" in packet:
                flags = int(str(packet.tcp.flags)[-3:])
                if flags & syn and flags & ack and packet.ip.dst == ip:
                    print ("Source: ", packet.ip.src, "\tDestination: ", packet.ip.dst)
                    ip_addr[packet.ip.src] += 1

    except AttributeError as ae:
        print("Attribute Error:", ae)

def flood_check():
    for ip in ip_addr.items():
        if ip[1] > 10:
            print("DDoS Attack Underway from ip ", ip[0])
            ip_addr[ip[0]] = 0

# For debugging purposes, use the code below

# our_ip = "172.22.8.1"

# packet_sniff(our_ip)