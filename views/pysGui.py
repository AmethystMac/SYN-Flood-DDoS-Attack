# Code-AMETHYST ver3.1
# TCP-SYN Flood Attack Detection GUI

# Modules
import sys
import os

# Directory Paths
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../"
SCRIPTS_DIR = PROJECT_DIR + "scripts/"
IMAGES_DIR = PROJECT_DIR + "images/"
sys.path.insert(0, SCRIPTS_DIR)

from PIL import ImageTk, Image
import tkinter as tk
import customtkinter as ctk
import threading
import socket
import pys

# GUI Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(SCRIPTS_DIR + "/app-theme.json")

# GUI
class GUI(ctk.CTk):
    # GUI Constructor
    def __init__(self):
        super().__init__()

        # Global variable initialization
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        self.this_ip = s.getsockname()[0]
        self.status = False

        # Main frame initialization
        self.title("MSFD")
        self.minsize(400, 480)
        self.maxsize(400, 480)

        self.frame1 = ctk.CTkFrame(master=self, width=400, height=600, fg_color="grey5", corner_radius=50)
        self.frame1.place(x=0, y=50)

        self.canvas1 = tk.Canvas(master=self.frame1, bg="grey5", height=450, highlightthickness=0, borderwidth=0)
        self.canvas1.create_line(45, 2, 335, 2, width=2, fill="white")

        self.canvas1.create_line(57, 50, 325, 50, width=2, fill="gray80")
        self.canvas1.create_line(57, 180, 325, 180, width=2, fill="gray80")
        self.canvas1.create_line(57, 215, 325, 215, width=2, fill="gray80")
        self.canvas1.create_line(57, 250, 325, 250, width=2, fill="gray80")

        self.canvas1.create_line(220, 25, 220, 40, width=2, fill="gray80")
        self.canvas1.create_line(220, 60, 220, 75, width=2, fill="gray80")
        self.canvas1.create_line(220, 155, 220, 170, width=2, fill="gray80")
        self.canvas1.create_line(220, 190, 220, 205, width=2, fill="gray80")
        self.canvas1.create_line(220, 225, 220, 240, width=2, fill="gray80")
        self.canvas1.create_line(220, 260, 220, 275, width=2, fill="gray80")

        self.canvas1.create_line(45, 380, 335, 380, width=2, fill="white")
        self.canvas1.place(x=10,y=20)

        self.image1 = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "black1.jpg").resize((50, 50)))
        self.image2 = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "alert2.jpg").resize((50, 50)))
        self.image3 = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "alert3.jpg").resize((50, 50)))

        self.label1 = ctk.CTkLabel(master=self, text="MATT'S SYN FLOOD DEFENDER", text_font=("", -18), text_color="grey5", fg_color="white", height=10, width=40)
        self.label1.place(x=60, y=15)

        self.label2 = ctk.CTkLabel(master=self, text="IP ADDRESS")
        self.label2.place(x=35, y=90)

        self.label3 = ctk.CTkLabel(master=self, text=self.this_ip, text_color="grey80", width=10)
        self.label3.place(x=265, y=90)

        self.label4 = ctk.CTkLabel(master=self, text="FIREWALL STATUS")
        self.label4.place(x=53, y=125)

        self.label5 = ctk.CTkLabel(master=self, text="TURNED OFF", text_color="red", width=100)
        self.label5.place(x=250, y=125)

        self.button1 = ctk.CTkButton(master=self, text="DEFEND", text_color="grey10", bg_color="grey10", corner_radius=4, height=30, width=200, command=self.flood_detect)
        self.button1.place(x=100, y=170)

        # Network Information
        self.label6 = ctk.CTkLabel(master=self, text="NETWORK STATUS")
        self.label6.place(x=54, y=220)

        self.label7 = ctk.CTkLabel(master=self, text="Turn On Firewall", text_color="gray80", width=100)
        self.label7.place(x=238, y=220)

        self.label8 = ctk.CTkLabel(master=self, text="WIRESHARK STATUS")
        self.label8.place(x=60, y=255)

        self.label9 = ctk.CTkLabel(master=self, text="Turn On Firewall", text_color="gray80", width=100)
        self.label9.place(x=237, y=255)

        self.label10 = ctk.CTkLabel(master=self, text="OUTGOING TRAFFIC")
        self.label10.place(x=57, y=290)

        self.label11 = ctk.CTkLabel(master=self, text="Turn On Firewall", text_color="gray80", justify="right", anchor="e", width=100)
        self.label11.place(x=235, y=290)

        self.label12 = ctk.CTkLabel(master=self, text="INCOMING TRAFFIC")
        self.label12.place(x=57, y=325)

        self.label13 = ctk.CTkLabel(master=self, text="Turn On Firewall", text_color="gray80", justify="right", anchor="e", width=100)
        self.label13.place(x=235, y=325)

        self.label14 = ctk.CTkLabel(master=self, text="SYN FLOOD DDOS\nATTACK UNDERWAY", text_color="gray5", text_font=("roboto", -18), justify="left", height=10, width=40)
        self.label14.place(x=140, y=370)
        
        self.panel1 = tk.Label(master=self, image=self.image1, border=0)
        self.panel1.place(x=85,y=370)

    # Firewall turned on
    def flood_detect(self):
        self.button1.configure(state="disabled")
        self.label5.configure(text="TURNED ON", text_color="lime")
        self.label7.configure(text="Working", text_color="lime")
        self.label7.place(x=261)
        self.label9.configure(text="Working", text_color="lime")
        self.label9.place(x=261)
        self.label11.configure(text="0.00 B/s")
        self.label11.place(x=235)
        self.label13.configure(text="0.00 B/s")
        self.label13.place(x=235)

        # Creating threads to keep processes away from each other
        thread1 = threading.Thread(target=pys.packet_sniff, args=(self.this_ip, ))
        thread2 = threading.Thread(target=pys.flood_check, args=(self.label14, self.panel1, self.image2, self.image3, ))
        thread3 = threading.Thread(target=pys.congestion_mech, args=(self.label7, ))
        thread4 = threading.Thread(target=pys.transmission_rate, args=(self.label11, self.label13, self.label14, self.panel1, self.image2, self.image3, ))

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