# Code-AMETHYST ver2.4
# PyShark GUI

# Modules
import sys
import os
pwd = os.path.dirname(os.path.abspath(__file__)) + "/../source"
sys.path.insert(0, pwd)

import tkinter as tk
import customtkinter as ctk
import threading
import socket
import pys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(pwd + "/green-theme.json")

# GUI
class GUI(ctk.CTk):
    # Functions
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

        self.label10 = ctk.CTkLabel(master=self, text="", text_color="red", text_font=("", -20), height=10, width=40)
        self.label10.place(x=60, y=280)

    def flood_detect(self):

        self.button1.configure(state="disabled")
        self.label5.configure(text="TURNED ON", text_color="lime")
        self.label7.configure(text="Working", text_color="lime")
        self.label9.configure(text="Working", text_color="lime")

        thread1 = threading.Thread(target=pys.packet_sniff, args=(self.this_ip, ))
        thread2 = threading.Thread(target=pys.flood_check, args=(self.label7, self.label10, ))

        thread1.start()
        thread2.start()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()