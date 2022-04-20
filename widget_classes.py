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
import sfgDF as solfege_DF


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
# purpose of this function is to create a solfege frame
# output: dict of {"solfege syllable": tk.Button(Frame,...)
# Foor easy handling on events.
class sfgFrame(tk.Frame):

    buttons = {}

    # Ran every time a new instance is created.
    # 'self' is ignored when we call Class.function
    # 'root' is from when we create the specific instance.
    def __init__(self, root, debug_text="debug text"):
        # Create a new dataframe to keep track of the buttons
        # and other constants
        self.sfgDF_class = solfege_DF.sfgDF()
        self.sfgDF = self.sfgDF_class.sfg_dict


        # Create the frame in which we will put all the sfg buttons
        # still don't get the Frame.__init but it's part of Frame
        tk.Frame.__init__(self, root)

        # what does .items() do again?
        for sfg_item in self.sfgDF.items():
            syllable = sfg_item[0]
            row = sfg_item[1]["row"]
            column = sfg_item[1]["column"]
            bgcolor = sfg_item[1]["bgcolor"]

            new_button = tk.Button(self, text=syllable, bg=bgcolor)
            new_button.grid(row=row,column=column, rowspan=1, columnspan=1)
            self.sfgDF[syllable]["tkButton"] = new_button




# fails is window.destroy is root.destroy...
# so somehow the literal word "root" is being
# transferred over
# But the name *doesn't* matter in BasicView
def close_win(e):
    print("exiting window...")
    window.destroy()


# for internal testing...
if __name__=='__main__':
    pass
    window = tk.Tk()
    window.geometry("700x350")
    window.bind('q', lambda e: close_win(e))

    view = sfgFrame(window)
    view.pack(side="top", fill="both", expand=True)
    print(view.sfgDF["le"]["tkButton"])
    print(view.sfgDF_class.sfg_dict["le"]["tkButton"])

    print(view.sfgDF["le"]["tkButton"] is view.sfgDF_class.sfg_dict["le"]["tkButton"])
   #print(view.main_sfg_names)

   #window.bind("a", key_down)
   #window.bind("<KeyRelease-a>", key_up)
   #window.bind("b", key_downdict)
   #window.bind("<KeyRelease-b>", key_updict)

   ## How to dynamically change some variable in there?
    window.mainloop()
