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
import widget_classes as widget_classes
#import keybind_helper as keybind_helper

def key_downdict(event):
    # switch event.keypress_name, case d... 1
    print(event)
    view.buttons["do"].configure(bg='blue')

def key_updict(event):
    print(event)
    view.buttons["do"].configure(bg=view.main_sfg_bg)

# How do I explicitely pass 'view' into this?
# I think that's all I need now...
# Also need to switch/ case on key_down

def close_win(e):
    print("exiting window...")
    window.destroy()

window = tk.Tk()
window.geometry("700x400")
window.bind('q', lambda e: close_win(e))
window.bind('j', lambda e: close_win(e))

# Create and display some sfg widgets
sfgFrame1 = widget_classes.sfgFrame(window)
sfgFrame2 = widget_classes.sfgFrame(window)
sfgFrame1.pack(side="left")
sfgFrame2.pack(side="right")

window.bind("b", key_downdict)
window.bind("<KeyRelease-b>", key_updict)

print(type(sfgFrame1))
print(type(sfgFrame1.sfgDF))

# To access the buttons: sfgFrame.sfgDF.sfg_dict["do"]

window.mainloop()
