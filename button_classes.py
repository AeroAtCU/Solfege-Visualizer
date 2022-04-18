# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://www.guru99.com/python-dictionary-append.html#6
# https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-geometry-managers/
# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
# def want .place(relx=X%, rely=Y%)
# probably want to define panes within the window. idk how.
# pack can work withing a frame, and within a... widget

#within the frame, I want a grid (?) using *rowconfigure*
import numpy as np
import tkinter as tk

def cmd_sfg(sfg, key="c"):
    print("Button pressed...")


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
def key_down(event):
    # switch event.keypress_name, case d... 1
    print(event)
    view.buttons[3].configure(bg='blue')

def key_up(event):
    print(event)
    view.buttons[3].configure(bg=view.main_sfg_bg)

# (tk.Frame) just means in inherets all the attributes from tk.Frame.
# It's not like a function argument.
class sfg_frame(tk.Frame):
    main_sfg_bg = "grey"
    flat_sfg_bg = "grey"
    sharp_sfg_bg = "grey"
    # key=sfg, value=# halfsteps away from do
    # value = no. half steps away from do note. also relates to grid position
    main_sfg_names = {
        "do": 1, "re": 3, "mi": 5, "fa": 6,
        "so": 8, "la": 10, "ti": 12 }
    flat_sfg_names = {
        "ra": 2, "me": 4, "se": 7,
        "le": 9, "te": 11 }
    sharp_sfg_names = {
        "di": 2, "ri": 4, "fi": 7,
        "si": 9, "li": 11 }

    # Store all created buttons (widgets) in a list
    buttons = {}

    # Ran every time a new instance is created.
    # 'self' is ignored when we call Class.function
    # 'root' is from when we create the specific instance.
    def __init__(self, root, debug_text="debug text"):
        # Create the frame in which we will put all the sfg buttons
        # still don't get the Frame.__init but it's part of Frame
        tk.Frame.__init__(self, root)

        # Create main solfege buttons
        # what ddoes .items() do again?
        # We use .items() to...
        for sfg_item in self.main_sfg_names.items():
            sfg_syllable = sfg_item[0]
            sfg_number = sfg_item[1]

            # Create the buttons, organize them
            new_button = tk.Button(self, text=sfg_syllable, bg=self.main_sfg_bg)
            new_button.grid(row=12-sfg_number,column=2, rowspan=1, columnspan=1)
            self.buttons[sfg_syllable] = new_button

        # Create sharp solfege buttons
        for sfg_item in self.sharp_sfg_names.items():
            sfg_syllable = sfg_item[0]
            sfg_number = sfg_item[1]

            new_button = tk.Button(self, text=sfg_syllable, bg=self.main_sfg_bg)
            new_button.grid(row=12-sfg_number, column=3, rowspan=2, columnspan=1)
            self.buttons[sfg_syllable] = new_button

        for sfg_item in self.flat_sfg_names.items():
            sfg_syllable = sfg_item[0]
            sfg_number = sfg_item[1]

            new_button = tk.Button(self, text=sfg_syllable, bg=self.main_sfg_bg)
            new_button.grid(row=12-sfg_number, column=1, rowspan=2, columnspan=1)
            self.buttons[sfg_syllable] = new_button



# fails is window.destroy is root.destroy...
# so somehow the literal word "root" is being
# transferred over
# But the name *doesn't* matter in BasicView
def close_win(e):
    print("exiting window...")
    window.destroy()

# for internal testing...
if __name__=='__main__':
    window = tk.Tk()
    window.geometry("700x350")
    
    view = sfg_frame(window)
    view.pack(side="top", fill="both", expand=True)
    print(view.buttons)
    print(view.main_sfg_names)
    print(view.buttons)

    window.bind("a", key_down)
    window.bind("<KeyRelease-a>", key_up)
    window.bind("b", key_downdict)
    window.bind("<KeyRelease-b>", key_updict)

    # How to dynamically change some variable in there?
    window.bind('q', lambda e: close_win(e))
    window.mainloop()
