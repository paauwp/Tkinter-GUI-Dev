import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class e_tkTK_Klasse_DistanceConverterStartScherm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Distance Converter")

        #ExtraFrameWindowContainer = ttk.Frame(self)
        #ExtraFrameWindowContainer.grid(padx=60, pady=30, sticky="EW")



        FrameScherm_MetersnaarVoeten = e_ttkFrame_Klasse_FrameScherm_MetersnaarVoeten(self, padding=(60,30))
        FrameScherm_MetersnaarVoeten.grid()

        self.bind("<Return>", FrameScherm_MetersnaarVoeten.Methode_Berekenvoeten)
        self.bind("<KP_Enter>", FrameScherm_MetersnaarVoeten.Methode_Berekenvoeten)

class e_ttkFrame_Klasse_FrameScherm_MetersnaarVoeten(ttk.Frame):
    def __init__(self,bewaarplek, **kwargs):
        super().__init__(bewaarplek, **kwargs)

        self.waarde_in_voeten = tk.StringVar()
        self.waarde_in_meters = tk.StringVar()

        meters_etiket = ttk.Label(self, text="metres")
        meters_invoer = ttk.Entry(self, width=10, textvariable=self.waarde_in_meters, font=(None, 15))  # None means "don't change the font".
        voeten_etiket = ttk.Label(self, text="feet")
        voeten_tonen = ttk.Label(self, textvariable=self.waarde_in_voeten)
        bereken_knop = ttk.Button(self, text="Calculate", command=self.Methode_Berekenvoeten)

        meters_etiket.grid(column=0, row=0, sticky="W")
        meters_invoer.grid(column=1, row=0, sticky="EW")
        meters_invoer.focus()

        voeten_etiket.grid(column=0, row=1, sticky="W")
        voeten_tonen.grid(column=1, row=1, sticky="EW")

        bereken_knop.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)


    def Methode_Berekenvoeten(self, *args):
        try:
            meters = float(self.waarde_in_meters.get())
            voeten = meters * 3.28084
            self.waarde_in_voeten.set(f"{voeten:.3f}")
        except ValueError:
             pass



StartScherm_Object = e_tkTK_Klasse_DistanceConverterStartScherm()

font.nametofont("TkDefaultFont").configure(size=15)

StartScherm_Object.columnconfigure(0, weight=1)

StartScherm_Object.mainloop()