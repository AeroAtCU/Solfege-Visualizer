import numpy as np
import tkinter as tk
#import button_classes.py
#from tkinter import Label

def up(event):
    print(event)
    print("a pressed")
    a.configure(bg='blue')


def up_release(event):
    print("a released")
    a.configure(bg='grey')


# Event to close the window
def close_win(e):
    print("exiting window...")
    root.destroy()

# Create main window
# root is the entire window
root = tk.Tk()
root.title("See Solfege!")

# Some graphic stuff...
root.geometry("700x350")
w = tk.Label(root, text="Solfege Visualizer\n Escape or q to quit") # Add label
#w.pack() # pack?
w.place(relx=0.2, rely=0.2)

# Close button and keypress bindings
close_button = tk.Button(root, text="Quit", command=root.destroy)
close_button.place(relx=0.1, rely=0.8)

a = tk.Button(root, text="color testing button")
a.configure(bg='red')
a.pack()
root.bind("a", up)
root.bind("<KeyRelease-a>", up_release)


#tk.Button(root, text="Quit", lambda e: close_win(e)).pack()#  why wouldn't this work? <- must be some difference with .Button vs .bind
root.bind('<Escape>', lambda e: close_win(e))
root.bind('q', lambda e: close_win(e))

# Test displaying image
canvas = tk.Canvas(root, width=100, height = 100)
canvas.place(relx=0.8, rely=0.8)
tkinter_image = tk.PhotoImage(file="img.png")
canvas.create_image(20, 20, image=tkinter_image)


# Must always run @ end to show the gui
root.mainloop()

print(__file__ + " end")


