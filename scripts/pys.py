# Code-AMETHYST ver2.7
# Back-end code for SYN Flood Attack Detector

# Modules
from collections import defaultdict
import time
import psutil
import customtkinter as ctk
import socket
import pyshark

# Global variables
ATTACK = False
TIMEUP = False
IP_ADDR = defaultdict(int)

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
                IP_ADDR[packet.ip.src] += 1

    except AttributeError as ae:
        print("Attribute Error:", ae)

def flood_check(label: ctk.CTkLabel):
    count = 0
    while(True):
        try:
            for ip in IP_ADDR.items():
                if ip[1] >= 1000:
                    global ATTACK

                    IP_ADDR.clear()
                    count += 1
                    
                    ATTACK = True
                    time.sleep(1)
                    ATTACK = False

                if count == 2:
                    count = 0
                    print("DDoS Warning: IP", ip[0])
                    display_attack(label)

        except RuntimeError as e:
            #print("Runtime Warning: Dictionary Size Changed.")
            pass

def display_cong(label: ctk.CTkLabel):
    print("Network Warning: There's a congestion in the network.")

    label.configure(text="Congested", text_color="red")

def remove_cong(label: ctk.CTkLabel):
    label.configure(text="Working", text_color="lime")

def congestion_mech(label: ctk.CTkLabel):
    displaying = False
    while True:
        if not displaying:
            if TIMEUP:
                display_cong(label)
                displaying = True

            elif ATTACK:
                display_cong(label)
                time.sleep(3)
                remove_cong(label)

        else:
            if not TIMEUP:
                remove_cong(label)
                displaying = False

def display_attack(label: ctk.CTkLabel):
    if TIMEUP:
        label.configure(text="ALERT: SYN FLOOD DDOS\nATTACK UNDERWAY")

def get_size(bytes: float):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}B/s"
        bytes /= 1024

def transmission_rate(label1: ctk.CTkLabel, label2: ctk.CTkLabel, label3: ctk.CTkLabel):
    global TIMEUP
    UPDATE_DELAY = 1

    io = psutil.net_io_counters()

    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    start, now = 0, 0
    while True:

        time.sleep(UPDATE_DELAY)

        io_2 = psutil.net_io_counters()

        us, ds = get_size((io_2.bytes_sent - bytes_sent) / UPDATE_DELAY), get_size((io_2.bytes_recv - bytes_recv) / UPDATE_DELAY)

        ds_split = ds.split(" ")
        if ds_split[1][0] == 'M' and float(ds_split[0][:3]) >= 1.5:
            TIMEUP = True
            if start == 0:
                start = time.time()
            now = time.time()
        else: TIMEUP = False

        if (now - start) >= 5:
            display_attack(label3)

        label1.configure(text=us)
        label2.configure(text=ds)

        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

# For debugging
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    our_ip = s.getsockname()[0]

    packet_sniff(our_ip)