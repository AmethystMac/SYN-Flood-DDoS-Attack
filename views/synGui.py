# Code-AMETHYST ver3.1
# TCP-SYN Flood Attack Simulation GUI

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
import syn

ctk.set_appearance_mode("light")
ctk.set_default_color_theme(SCRIPTS_DIR + "/app-theme.json")

# Main Class
class GUI(ctk.CTk):
    # GUI Constructor
    def __init__(self):
        super().__init__()

        # General variable initialization
        self.count = 0

        # Main frame initialization
        self.title("MSFS")
        self.minsize(400, 480)
        self.maxsize(400, 480)

        self.frame1 = ctk.CTkFrame(master=self, width=400, height=600, fg_color="white", corner_radius=50)
        self.frame1.place(x=0, y=50)

        self.canvas1 = tk.Canvas(master=self.frame1, bg="white", height=450, highlightthickness=0, borderwidth=0)
        self.canvas1.create_line(45, 2, 335, 2, width=2, fill="grey25")
        self.canvas1.create_line(45, 380, 335, 380, width=2, fill="grey25")
        self.canvas1.place(x=10,y=20)

        self.image1 = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "white1.jpg").resize((25, 25)))
        self.image2 = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "alert1.jpg").resize((25, 25)))

        # Basic Mode
        self.label1 = ctk.CTkLabel(master=self, text="MATT'S SYN FLOOD SIMULATOR", text_font=("", -18), text_color="white", fg_color="grey5", height=10, width=40)
        self.label1.place(x=55, y=15)

        self.label2 = ctk.CTkLabel(master=self, text="IP ADDRESS", text_color="grey25")
        self.label2.place(x=40, y=80)

        self.entry1 = ctk.CTkEntry(master=self, placeholder_text="Enter IP", bg_color="white", corner_radius=4, height=30, width=200)
        self.entry1.place(x=72, y=102)

        self.button1 = ctk.CTkButton(master=self, text="ATTACK", text_color="white", bg_color="white", corner_radius=4, height=30, width=200, command=self.field_check)
        self.button1.place(x=72, y=150)

        self.label3 = ctk.CTkLabel(master=self, text="STATUS", text_color="grey25")
        self.label3.place(x=27, y=193)

        self.label8 = ctk.CTkLabel(master=self, text="FREE", text_color="green")
        self.label8.place(x=188, y=193)

        self.label4 = ctk.CTkLabel(master=self, text="ADVANCED", text_color="grey25")
        self.label4.place(x=37, y=225)

        self.switch = ctk.CTkSwitch(master=self, text="", onvalue="on", offvalue="off", bg_color="white", command=self.adv_switch)
        self.switch.place(x=240, y=230)

        # Advanced Mode
        self.label5 = ctk.CTkLabel(master=self, text="PORT", text_color="grey25")
        self.label5.place(x=20, y=260)

        self.entry2 = ctk.CTkEntry(master=self, placeholder_text="443", bg_color="white", corner_radius=4, height=30, width=200)
        self.entry2.place(x=72, y=282)
        self.entry2.configure(state="disabled")

        self.label6 = ctk.CTkLabel(master=self, text="PACKET COUNT", text_color="grey25")
        self.label6.place(x=51, y=320)

        self.entry3 = ctk.CTkEntry(master=self, placeholder_text="10000", bg_color="white", corner_radius=4, height=30, width=200)
        self.entry3.place(x=72, y=342)
        self.entry3.configure(state="disabled")

        self.label7 = ctk.CTkLabel(master=self, text="INTENSITY", text_color="grey25")
        self.label7.place(x=36, y=380)

        self.slider = ctk.CTkSlider(master=self, number_of_steps=2, state="disabled", bg_color="white")
        self.slider.place(x=72, y=405)
        self.slider.set(0)

        # Error Labels
        self.panel1 = tk.Label(master=self, image=self.image1, border=0)
        self.panel1.place(x=275,y=102)

        self.label9 = ctk.CTkLabel(master=self, text="", text_color="grey25", width=50)
        self.label9.place(x=300, y=102)

        self.panel2 = tk.Label(master=self, image=self.image1, border=0)
        self.panel2.place(x=275,y=282)

        self.label10 = ctk.CTkLabel(master=self, text="", text_color="grey25", width=50)
        self.label10.place(x=300, y=282)

        self.panel3 = tk.Label(master=self, image=self.image1, border=0)
        self.panel3.place(x=275,y=342)

        self.label11 = ctk.CTkLabel(master=self, text="", text_color="grey25", width=50)
        self.label11.place(x=300, y=342)

    # Advanced Mode On/Off
    def adv_switch(self):
        mode = self.switch.get()
        if mode == "on":
            print("Advanced mode: ON")
            self.entry2.configure(state="normal")
            self.entry3.configure(state="normal")
            self.slider.configure(state="normal")

        else:
            print("Advanced mode: OFF")
            self.panel2.configure(image=self.image1)
            self.panel3.configure(image=self.image1)
            self.label10.configure(text="")
            self.label11.configure(text="")

            self.entry2.delete(0, 100)
            self.entry2.configure(placeholder_text="443")
            self.entry2.configure(state="disabled")

            self.entry3.delete(0, 100)
            self.entry3.configure(placeholder_text="10000")
            self.entry3.configure(state="disabled")

            self.slider.set(0)
            self.slider.configure(state="disabled")

    # Method to check the input fields for valid input
    def field_check(self):
        mode = self.switch.get()

        if mode == "on":
            ip = self.entry1.get().split('.')
            port = self.entry2.get()
            packets = self.entry3.get()
            intensity = self.slider.get()
            flag = True

            self.panel1.configure(image=self.image1)
            self.panel2.configure(image=self.image1)
            self.panel3.configure(image=self.image1)

            self.label9.configure(text="")
            self.label10.configure(text="")
            self.label11.configure(text="")

            if len(ip) != 4:
                self.panel1.configure(image=self.image2)
                self.label9.configure(text="ERROR!")
                flag = False

            if not port.isdigit():
                self.panel2.configure(image=self.image2)
                self.label10.configure(text="ERROR!")
                flag = False

            if not packets.isdigit():
                self.panel3.configure(image=self.image2)
                self.label11.configure(text="ERROR!")
                flag = False

            if flag:
                self.attack(int(port), int(int(packets) * (float(intensity) + 0.5) * 2))

        else:
            ip = self.entry1.get().split('.')

            if len(ip) != 4:
                self.panel1.configure(image=self.image2)
                self.label9.configure(text="ERROR!")

            else:
                self.attack()

    # Start attack
    def attack(self, port: int = 443, packets: int = 10000):
        self.panel1.configure(image=self.image1)
        self.panel2.configure(image=self.image1)
        self.panel3.configure(image=self.image1)

        self.label9.configure(text="")
        self.label10.configure(text="")
        self.label11.configure(text="")

        ip = self.entry1.get()

        thread = threading.Thread(target=syn.send_syn, args=(ip, port, packets, self.label8, self.count, ))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()