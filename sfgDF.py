import tkinter as tk

class sfgDF(tk.Frame):
    testval = "c"
    sfg_dict = {}

    if True:
        # hardcoded data for each "base" tpe of sfg (drmfslt)
        sfg_dict["do"] = {"row":11, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":0}
        sfg_dict["re"] = {"row":9, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":2}
        sfg_dict["mi"] = {"row":7, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":4}
        sfg_dict["fa"] = {"row":6, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":5}
        sfg_dict["so"] = {"row":4, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":7}
        sfg_dict["la"] = {"row":2, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":9}
        sfg_dict["ti"] = {"row":0, "column":1, "type":"base",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":11}

        # hardcoded data for each "sharp" tpe of sfg (di,ri)
        sfg_dict["di"] = {"row":7, "column":2, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "octave":3, "halfsteps":1}
        sfg_dict["ri"] = {"row":6, "column":2, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "octave":3, "halfsteps":3}
        sfg_dict["fi"] = {"row":4, "column":2, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "octave":3, "halfsteps":6}
        sfg_dict["si"] = {"row":2, "column":2, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "octave":3, "halfsteps":8}
        sfg_dict["li"] = {"row":0, "column":2, "type":"sharp",
                "bgcolor":"grey", "activecolor":"red",
                "octave":3, "halfsteps":10}

        # hardcoded data for each "flat" type of sfg (me,re)
        sfg_dict["ra"] = {"row":7, "column":0, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":1}
        sfg_dict["me"] = {"row":6, "column":0, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":3}
        sfg_dict["se"] = {"row":4, "column":0, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":6}
        sfg_dict["le"] = {"row":2, "column":0, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":8}
        sfg_dict["te"] = {"row":0, "column":0, "type":"flat",
                "bgcolor":"grey", "activecolor":"blue",
                "octave":3, "halfsteps":10}

    def get_sfg_dict(self):
        return self.sfg_dict

    def get_key(self):
        pass

    def set_key(self, key):
        pass


#window = tk.Tk()
#a = sfgDF(window)
   #b = a.get_sfg_dict()
   #c = sfgDF(window).get_sfg_dict()
   #print(b)
   #print(b["do"]["row"])

