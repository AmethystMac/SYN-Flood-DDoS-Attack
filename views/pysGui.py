# PyShark GUI

# Modules
import sys

sys.path.insert(0, "//home/kali/Desktop/SYN-Flood-DDoS-Attack/source")

from tkinter import *
import threading
import pys

# Functions
def flood_detect():

    this_ip = "172.22.8.1"

    thread1 = threading.Thread(target = pys.packet_sniff, args = (this_ip, ))
    thread2 = threading.Thread(target = pys.flood_check)

    thread1.start()
    thread2.start()

# GUI
root = Tk()
root.geometry("200x200")

label = Label(root, text = "foo")
button1 = Button(root, text = "detecc", command = flood_detect)
button2 = Button(root, text = "destroy", command = root.destroy)

label.pack()
button1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()