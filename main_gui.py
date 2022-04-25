#https://stackoverflow.com/questions/27215326/tkinter-keypress-keyrelease-events
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://www.guru99.com/python-dictionary-append.html#6
# https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-geometry-managers/
# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
# def want .place(relx=X%, rely=Y%)
# probably want to define panes within the window. idk how.
# pack can work withing a frame, and within a... widget

#within the frame, I want a grid (?) using *rowconfigure* 
import tkinter as tk
import widget_classes as wc

import keybind_event_handler as kbh
from keybind_event_handler import * # To get variables...


   #ALL_SOLFEGE = set(["do", "re", "mi", "fa", "so", "la", "ti", "di", "ri", "fi", "si", "li", "ra", "me", "se", "le", "te"])
   #VALID_KEYS = set(["d", "d", "i", "e", "r", "m", "f", "s", "l", "t"])
   #GLOBAL_STATE = { "keys": set() }


# No matter what, I need to pass information into the keypress function.
def kd(event, sfgFrame):
    sfgFrame.sfgDF["do"]["tkButton"].configure(bg=sfgFrame.sfgDF["do"]["activecolor"])

def ku(event, sfgFrame):
    sfgFrame.sfgDF["do"]["tkButton"].configure(bg=sfgFrame.sfgDF["do"]["bgcolor"])

def close_win(e, windowToDel):
    print("exiting window...")
    windowToDel.destroy()

window = tk.Tk()
window.geometry("700x400")
window.bind('q', lambda e: close_win(e, window)) # explicitely close this window
window.bind('j', lambda e: close_win(e, window))

# Create and display some sfg widgets
sfgFrame1 = wc.sfgFrame(window)
sfgFrame2 = wc.sfgFrame(window)
sfgFrame1.pack(side="left")
sfgFrame2.pack(side="right")

# okay, this allows me to send info to the function now alongwith the event
window.bind("c", lambda event: kd(event=event, sfgFrame=sfgFrame2))
window.bind("<KeyRelease-c>", lambda event: ku(event=event, sfgFrame=sfgFrame2))

for k in VALID_KEYS:
    window.bind(k, lambda event: kbh.key_press_event(event=event, sfgFrame=sfgFrame1))
    window.bind(f"<KeyRelease-{k}>", lambda event: kbh.key_release_event(event=event, sfgFrame=sfgFrame1))


# To access the buttons: sfgFrame.sfgDF.sfg_dict["do"]
window.mainloop()
