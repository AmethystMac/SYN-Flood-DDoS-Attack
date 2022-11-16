import pyshark

# capture = pyshark.FileCapture("/home/kali/Desktop/wsCapture.pcapng")    # Importing the capture file

# for packet in capture:      # Iterating through the packets in the file
#     print(packet.ip.src)    # Printing the source address of the packet
#     print(packet.ip.dst, "\n")    # Printing the destination address of the packets

source_ip = "172.22.10.40"
destination_ip = "34.102.187.140"

capture = pyshark.LiveCapture(interface='eth0')

try:
    for packet in capture.sniff_continuously():
        if "IP" in packet and packet.ip.src == source_ip:
            print ("Source: ", packet.ip.src, "   Destination: ", packet.ip.dst)

except AttributeError:
    print("Attribute Error: Try Again")