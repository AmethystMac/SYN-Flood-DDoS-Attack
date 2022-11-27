# Code-AMETHYST ver2.4
# TCP-SYN Flood Attack Simulation GUI

# Modules
import sys
import os
pwd = os.path.dirname(os.path.abspath(__file__)) + "/../source"
sys.path.insert(0, pwd)

import threading
import tkinter as tk
import customtkinter as ctk
import syn

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Main Class
class GUI(ctk.CTk):
    # Functions
    def __init__(self):
        super().__init__()

        # General variable initialization
        self.count = 0

        # Main frame initialization
        self.title("MSFS")
        self.minsize(400, 400)
        self.maxsize(400, 400)

        # Basic Mode
        self.label1 = ctk.CTkLabel(master=self, text="MATT'S SYN FLOOD SIMULATOR", text_font=("Roboto Medium", -18), height=10, width=40)
        self.label1.place(x=60, y=20)

        self.label2 = ctk.CTkLabel(master=self, text="IP Address:", height=10, width=40)
        self.label2.place(x=10, y=60)

        self.entry1 = ctk.CTkEntry(master=self)
        self.entry1.place(x=100, y=55)

        self.button = ctk.CTkButton(master=self, text="Attack", command=self.field_check)
        self.button.place(x=100, y=100)

        self.label3 = ctk.CTkLabel(master=self, text="Advanced:", height=10, width=40)
        self.label3.place(x=10, y=180)

        self.switch = ctk.CTkSwitch(master=self, text="", onvalue="on", offvalue="off", command=self.adv_switch)
        self.switch.place(x=100, y=180)

        self.label8 = ctk.CTkLabel(master=self, text="Status:", height=10, width=40)
        self.label8.place(x=10, y=140)

        self.label9 = ctk.CTkLabel(master=self, text="FREE", text_color="lime", height=10, width=40)
        self.label9.place(x=95, y=140)

        # Advanced Mode
        self.label4 = ctk.CTkLabel(master=self, text="Port:", height=10, width=40)
        self.label4.place(x=5, y=220)

        self.entry2 = ctk.CTkEntry(master=self, placeholder_text="default=443", state="disabled")
        self.entry2.place(x=100, y=215)

        self.label5 = ctk.CTkLabel(master=self, text="Packets:", height=10, width=40)
        self.label5.place(x=10, y=270)

        self.entry3 = ctk.CTkEntry(master=self, placeholder_text="default=10000", state="disabled")
        self.entry3.place(x=100, y=265)

        self.label6 = ctk.CTkLabel(master=self, text="Intensity:", height=10, width=40)
        self.label6.place(x=10, y=318)

        self.slider = ctk.CTkSlider(master=self, number_of_steps=2, state="disabled")
        self.slider.place(x=100, y=320)
        self.slider.set(0)

        self.label7 = ctk.CTkLabel(master=self, text="", text_color="red", height=10, width=40)
        self.label7.place(x=100, y=360)

    def adv_switch(self):

        mode = self.switch.get()
        if mode == "on":
            print("Advanced mode: ON")
            self.entry2.configure(state="normal")
            self.entry3.configure(state="normal")
            self.slider.configure(state="normal")

        else:
            print("Advanced mode: OFF")
            self.entry2.configure(state="disabled")
            self.entry3.configure(state="disabled")
            self.slider.configure(state="disabled")

    # Function that checks the input fields for valid input
    def field_check(self):
        mode = self.switch.get()
        flag = True
        
        ip = self.entry1.get().split('.')
        if len(ip) != 4:
            self.label7.configure(text="ERROR: Enter a valid IP Address!")
            flag = False

        if mode == "on":
            port = self.entry2.get()
            packets = self.entry3.get()
            if not port.isdigit():
                self.label7.configure(text="ERROR: Enter a valid Port!")
                flag = False

            elif not packets.isdigit():
                self.label7.configure(text="ERROR: Enter a valid Packets Count!")
                flag = False

            if flag:
                self.attack(int(port), int(packets))

        else:
            if flag:
                self.attack()

    def attack(self, port: int = 443, packets: int = 10000):
        self.label7.configure(text="")

        ip = self.entry1.get()
        
        thread = threading.Thread(target = syn.send_syn, args = (ip, port, packets, self.label9, self.count, ))
        thread.start()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()