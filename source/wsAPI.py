import pyshark

source_ip = "172.22.8.1"
destination_ip = "172.22.8.1"

syn = 2
ack = 10

capture = pyshark.LiveCapture(interface='eth0')

try:
    for packet in capture.sniff_continuously():
        if "IP" in packet and "TCP" in packet:
            flags = int(str(packet.tcp.flags)[-3:])
            if flags & syn and flags & ack:
                print ("Source: ", packet.ip.src, "   Destination: ", packet.ip.dst)

except AttributeError as ae:
    print("Attribute Error:", ae)