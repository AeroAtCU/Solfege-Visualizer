import numpy as np
import time as time
import tkinter as tk
#from tkinter import Label

# Event to close the window
def close_win(e):
    print("exiting window...")
    root.destroy()

#   class BasicView(tk.Frame):
#       def __init__(self, root):
#           tk.Frame.__init__(self, root)
#           l = tk.Label(self, text="some text", anchor="c")
#           l.pack(side="top", fill="both", expand=True)

#   if __name__=='__main__':
#       root = tk.Tk()
#       view = BasicView(root)
#       view.pack(side="top", fill="both", expand=True)
#       root.mainloop()

# Create main window
root = tk.Tk()

# Some graphic stuff...
root.geometry("700x350")
w = tk.Label(root, text="Solfege Visualizer\n Escape or q to quit") # Add label
w.pack() # pack?

# Close button and keypress
tk.Button(root, text="Quit", command=root.destroy).pack()
#tk.Button(root, text="Quit", lambda e: close_win(e)).pack()#  why wouldn't this work?
root.bind('<Escape>', lambda e: close_win(e))
root.bind('q', lambda e: close_win(e))

# Keep window alive
root.mainloop()

print("basic_graphics.py end")
