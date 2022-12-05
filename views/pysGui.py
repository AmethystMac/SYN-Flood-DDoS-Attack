# Code-AMETHYST ver2.7
# PyShark GUI

# Modules
import sys
import os
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"
SCRIPTS_DIR = PROJECT_DIR + "scripts/"
IMAGES_DIR = PROJECT_DIR + "images/"
sys.path.insert(0, SCRIPTS_DIR)

import tkinter as tk
import customtkinter as ctk
import threading
import socket
import pys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(SCRIPTS_DIR + "/green-theme.json")

# GUI
class GUI(ctk.CTk):
    # Methods
    def __init__(self):
        super().__init__()

        # Global variable initialization
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        self.this_ip = s.getsockname()[0]
        self.status = False

        # Main frame initialization
        self.title("MSFD")
        self.minsize(400, 400)
        self.maxsize(400, 400)

        self.label1 = ctk.CTkLabel(master=self, text="MATT'S SYN FLOOD DEFENDER", text_font=("", -18), height=10, width=40)
        self.label1.place(x=60, y=15)

        self.label2 = ctk.CTkLabel(master=self, text="IP Address: ", height=10, width=40)
        self.label2.place(x=10, y=60)

        self.label3 = ctk.CTkLabel(master=self, text=self.this_ip, text_font=("", -14), height=10, width=40)
        self.label3.place(x=120, y=60)

        self.button1 = ctk.CTkButton(master=self, text="Defend", command=self.flood_detect)
        self.button1.place(x=120, y=95)

        self.label4 = ctk.CTkLabel(master=self, text="Firewall Status: ", height=10, width=40)
        self.label4.place(x=10, y=140)

        self.label5 = ctk.CTkLabel(master=self, text="TURNED OFF", text_color="red", height=10, width=40)
        self.label5.place(x=120, y=140)

        self.label6 = ctk.CTkLabel(master=self, text="Network Status: ", height=10, width=40)
        self.label6.place(x=10, y=180)

        self.label7 = ctk.CTkLabel(master=self, text="Turn on Firewall", height=10, width=40)
        self.label7.place(x=120, y=180)

        self.label8 = ctk.CTkLabel(master=self, text="WireShark Status: ", height=10, width=40)
        self.label8.place(x=10, y=220)

        self.label9 = ctk.CTkLabel(master=self, text="Turn on Firewall", height=10, width=40)
        self.label9.place(x=120, y=220)

        self.label10 = ctk.CTkLabel(master=self, text="Outgoing Traffic: ", height=10, width=40)
        self.label10.place(x=10, y=260)

        self.label11 = ctk.CTkLabel(master=self, text="Turn on Firewall", height=10, width=40)
        self.label11.place(x=120, y=260)

        self.label12 = ctk.CTkLabel(master=self, text="Incoming Traffic: ", height=10, width=40)
        self.label12.place(x=10, y=300)

        self.label13 = ctk.CTkLabel(master=self, text="Turn on Firewall", height=10, width=40)
        self.label13.place(x=120, y=300)

        self.label14 = ctk.CTkLabel(master=self, text="", text_color="red", text_font=("", -18), height=10, width=40)
        self.label14.place(x=80, y=340)

    def flood_detect(self):
        self.button1.configure(state="disabled")
        self.label5.configure(text="TURNED ON", text_color="lime")
        self.label7.configure(text="Working", text_color="lime")
        self.label9.configure(text="Working", text_color="lime")
        self.label11.configure(text="0.00 B/s")
        self.label13.configure(text="0.00 B/s")

        thread1 = threading.Thread(target=pys.packet_sniff, args=(self.this_ip, ))
        thread2 = threading.Thread(target=pys.flood_check, args=(self.label14, ))
        thread3 = threading.Thread(target=pys.congestion_mech, args=(self.label7, ))
        thread4 = threading.Thread(target=pys.transmission_rate, args=(self.label11, self.label13, self.label14, ))

        thread1.daemon = True
        thread2.daemon = True
        thread3.daemon = True
        thread4.daemon = True

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()