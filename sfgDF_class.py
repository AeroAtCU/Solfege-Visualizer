import tkinter as tk

# a solfegge dataframe
# Holds all information needed to create the GUI, each syllables musical parameters, and the tk.Button object that is actually displayed
class sfgDF(tk.Frame):
    def __init__(self):
        self.sfg_dict = {}

        # hardcoded data for each "base" tpe of sfg (drmfslt)
        self.sfg_dict["do"] = {"row":11, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":0}
        self.sfg_dict["re"] = {"row":10, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":2}
        self.sfg_dict["mi"] = {"row":9, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":4}
        self.sfg_dict["fa"] = {"row":8, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":5}
        self.sfg_dict["so"] = {"row":7, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":7}
        self.sfg_dict["la"] = {"row":6, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":9}
        self.sfg_dict["ti"] = {"row":5, "column":1, "rowspan":1, "columnspan":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":11}

        # hardcoded data for each "sharp" tpe of sfg (di,ri)
        self.sfg_dict["di"] = {"row":10, "column":2, "rowspan":2, "columnspan":1, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "halfsteps":1}
        self.sfg_dict["ri"] = {"row":9, "column":2, "rowspan":2, "columnspan":1, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "halfsteps":3}
        self.sfg_dict["fi"] = {"row":7, "column":2, "rowspan":2, "columnspan":1, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "halfsteps":6}
        self.sfg_dict["si"] = {"row":6, "column":2, "rowspan":2, "columnspan":1, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "halfsteps":8}
        self.sfg_dict["li"] = {"row":5, "column":2, "rowspan":2, "columnspan":1, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "halfsteps":10}

        # hardcoded data for each "flat" type of sfg (me,re)
        self.sfg_dict["ra"] = {"row":10, "column":0, "rowspan":2, "columnspan":1, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":1}
        self.sfg_dict["me"] = {"row":9, "column":0, "rowspan":2, "columnspan":1, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":3}
        self.sfg_dict["se"] = {"row":7, "column":0, "rowspan":2, "columnspan":1, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":6}
        self.sfg_dict["le"] = {"row":6, "column":0, "rowspan":2, "columnspan":1, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":8}
        self.sfg_dict["te"] = {"row":5, "column":0, "rowspan":2, "columnspan":1, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "halfsteps":10}


    def get_sfg_dict(self):
        return self.sfg_dict


# for internal testing...
if __name__=='__main__':
    pass
