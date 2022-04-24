import numpy as np
import tkinter as tk
import sfgDF_class as sfgDF_class
# Should I just turn this whole thing into a function instead of a class? All it does is loop thru the sfgDF and create buttons... yea
# Just have it return [tk.Frame, sfgDF]. right? and just store anything else I need in the sfgDF like octave or whatever. doesn't need to be a whole class.

# (tk.Frame) just means in inherets all the attributes from tk.Frame.  It's not like a function argument.
# Purpose: create a Frame which contains the entire solfege "stack" and the corresponding sfgDF that contains o create a solfege frame... wait
# output: dict of {"solfege syllable": tk.Button(Frame,...)
# For easy handling on events.
class sfgFrame(tk.Frame):
    def __init__(self, root, debug_text="debug text"):
        # Create a new dataframe to keep track of the buttons and other constants
        self.sfgDF = sfgDF_class.sfgDF()

        # Create the frame in which we will put all the sfg buttons
        # Accessible directly from the sfgFrame object
        tk.Frame.__init__(self, root)

        # what does .items() do again?
        for sfg_item in self.sfgDF.sfg_dict.items():
            # Extract the syllable and dict of data
            syllable = sfg_item[0]
            syllable_data = sfg_item[1]

            # for readabiility, extract the information used
            row = syllable_data["row"]
            column = syllable_data["column"]
            rowspan = syllable_data["rowspan"]
            bgcolor = syllable_data["bgcolor"]

            # create the button, add it to the Frame grid, & store the obj in it's syllables dict
            new_button = tk.Button(self, text=syllable, bg=bgcolor)
            new_button.grid(row=row,column=column, rowspan=rowspan, columnspan=1)
            self.sfgDF.sfg_dict[syllable]["tkButton"] = new_button



# for internal testing...
if __name__=='__main__':
    pass
