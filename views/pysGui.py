# Code-AMETHYST ver2.4
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
    thread2 = threading.Thread(target = pys.flood_check, args = (label2, ))

    thread1.start()
    thread2.start()

# GUI
def main():
    root = Tk()
    root.title("Defender")
    root.geometry("400x400")

    label1 = Label(root, text = "MATTHEW'S SYN FLOOD DEFENDER")
    label2 = Label(root, text = "SAFE")
    button1 = Button(root, text = "detecc", command = flood_detect)
    button2 = Button(root, text = "destroy", command = root.destroy)

    label1.pack()
    label2.pack()
    button1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()