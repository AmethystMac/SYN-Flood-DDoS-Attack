# Code-AMETHYST ver2.4
# Back-end code for SYN Flood Attack Detector

# Modules
from collections import defaultdict
from tkinter import *
import pyshark

# Global variables
ip_addr = defaultdict(int)

# Functions
def packet_sniff(ip: str):

    syn = 2
    ack = 10

    capture = pyshark.LiveCapture(interface='eth0')

    try:
        for packet in capture.sniff_continuously():
            if "IP" in packet:
            #   flags = int(str(packet.tcp.flags)[-3:])
            #   if flags & syn and flags & ack and packet.ip.dst == ip:
            #   print ("Source: ", packet.ip.src, "\tDestination: ", packet.ip.dst)
                ip_addr[packet.ip.src] += 1

    except AttributeError as ae:
        print("Attribute Error:", ae)

def flood_check(label: str):
    max = ("", 0)
    while(True):
        try:
            for ip in ip_addr.items():
                if ip[1] > max[1]:
                    max = ip
                if max[1] > 1000:
                    print("DDoS Attack Underway from ip ", max[0])
                    ip_addr[max[0]] = 0
                    display_attack(label)
        except RuntimeError as e:
            print("Runtime Error: Dictionary Size Changed.")

def display_attack(label: str):
    if label.cget("text") != "ATTACKKKK":
        label.config(text="ATTACKKKK")

# For debugging purposes, use the code below

# our_ip = "172.22.8.1"
# packet_sniff(our_ip)