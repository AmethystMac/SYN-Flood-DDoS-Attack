# Code-AMETHYST ver3.1
# Back-end code for SYN Flood Attack Detector

# Modules
from collections import defaultdict
from PIL import ImageTk, Image
import time
import psutil
import tkinter as tk
import customtkinter as ctk
import threading
import socket
import pyshark

# Global variables
ATTACK = False
ATTACK_DISPLAY = False
TIMEUP = False
IP_ADDR = defaultdict(int)

# Using PyShark to sniff the incoming SYN packets
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

# Method that keeps track of status of the congestion in the network
def flood_check(label: ctk.CTkLabel, panel: tk.Label, alert_img1: ImageTk.PhotoImage, alert_img2: ImageTk.PhotoImage):
    global ATTACK_DISPLAY

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
                    if not ATTACK_DISPLAY:
                        thread = threading.Thread(target=display_attack, args=(label, panel, alert_img1, alert_img2, ))
                        thread.start()

                        ATTACK_DISPLAY = True

        except RuntimeError as e:
            #print("Runtime Warning: Dictionary Size Changed.")
            pass

# Display congestion
def display_cong(label: ctk.CTkLabel):
    print("Network Warning: There's a congestion in the network.")

    label.configure(text="Congested", text_color="red")
    label.place(x=253)

# Stop displaying congestion
def remove_cong(label: ctk.CTkLabel):
    label.configure(text="Working", text_color="lime")
    label.place(x=261)

# Congestion mechanism
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

# Find the byte size
def get_size(bytes: float):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}B/s"
        bytes /= 1024

# Network monitor
def transmission_rate(label1: ctk.CTkLabel, label2: ctk.CTkLabel, label3: ctk.CTkLabel, panel: tk.Label, alert_img1: ImageTk.PhotoImage, alert_img2: ImageTk.PhotoImage):
    global TIMEUP, ATTACK_DISPLAY
    update_delay = 1

    io = psutil.net_io_counters()

    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    start, now = 0, 0
    while True:

        time.sleep(update_delay)

        io_2 = psutil.net_io_counters()

        us, ds = get_size((io_2.bytes_sent - bytes_sent) / update_delay), get_size((io_2.bytes_recv - bytes_recv) / update_delay)

        ds_split = ds.split(" ")
        if ds_split[1][0] == 'M' and float(ds_split[0][:3]) >= 1.5:
            TIMEUP = True
            if start == 0:
                start = time.time()
            now = time.time()
        else: TIMEUP = False

        if (now - start) >= 5 and not ATTACK_DISPLAY:
            thread = threading.Thread(target=display_attack, args=(label3, panel, alert_img1, alert_img2, ))
            thread.start()

            ATTACK_DISPLAY = True

        label1.configure(text=us)
        label2.configure(text=ds)

        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

# Attack alert mechanism
def display_attack(label: ctk.CTkLabel, panel: tk.Label, alert_img1: ImageTk.PhotoImage, alert_img2: ImageTk.PhotoImage):
    if TIMEUP:
        while True:
            panel.configure(image=alert_img2)
            label.configure(text_color="red")
            time.sleep(0.1)
            panel.configure(image=alert_img1)
            label.configure(text_color="white")
            time.sleep(0.1)

# For debugging
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    our_ip = s.getsockname()[0]

    packet_sniff(our_ip)