# Code-AMETHYST ver2.4
# Back-end code for SYN Flood Attack Detector

# Modules
from collections import defaultdict
from time import sleep
import customtkinter as ctk
import threading
import socket
import pyshark

# Global variables
attack = False
ip_addr = defaultdict(int)

# Functions
def packet_sniff(ip: str):

    syn = 2
    ack = 10

    capture = pyshark.LiveCapture(interface='eth0')

    try:
        for packet in capture.sniff_continuously():
            if "IP" in packet:
            #    flags = int(str(packet.tcp.flags)[-3:])
            #    if packet.ip.dst == ip:
            #    print ("Source: ", packet.ip.src, "\tDestination: ", packet.ip.dst)
                ip_addr[packet.ip.src] += 1

    except AttributeError as ae:
        print("Attribute Error:", ae)

def flood_check(label1: ctk.CTkLabel, label2: ctk.CTkLabel):
    count = 0
    while(True):
        try:
            for ip in ip_addr.items():
                if ip[1] >= 500:
                    ip_addr[ip[0]] = 0
                    count += 1

                    thread = threading.Thread(target=stall, args=(label1, ))
                    thread.start()

                if count == 2:
                    count = 0
                    print("DDoS Attack Underway from IP", ip[0])
                    display_attack(label2)

        except RuntimeError as e:
            print("Runtime Error: Dictionary Size Changed.")

def stall(label: ctk.CTkLabel):
    print("inside stall")
    label.configure(text="Congested", text_color="red")
    sleep(3)
    label.configure(text="Working", text_color="lime")

def display_attack(label: ctk.CTkLabel):
    if not attack:
        label.configure(text="ALERT: SYN FLOOD DDOS\nATTACK UNDERWAY")

# For debugging purposes, use the code below

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 1))
# our_ip = s.getsockname()[0]

# packet_sniff(our_ip)