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

        ExtraFrameWindowContainer = ttk.Frame(self)
        ExtraFrameWindowContainer.grid(padx=60, pady=30, sticky="EW")

        FrameScherm_MetersnaarVoeten = e_ttkFrame_Klasse_FrameScherm_MetersnaarVoeten(ExtraFrameWindowContainer)
        FrameScherm_MetersnaarVoeten.grid(row=0, column=0, sticky="NSEW")

        self.bind("<Return>", FrameScherm_MetersnaarVoeten.Methode_Bereken)
        self.bind("<KP_Enter>", FrameScherm_MetersnaarVoeten.Methode_Bereken)

class e_ttkFrame_Klasse_FrameScherm_MetersnaarVoeten(ttk.Frame):
    def __init__(self,bewaarplek, **kwargs):
        super().__init__(bewaarplek, **kwargs)

        self.waarde_in_voeten = tk.StringVar()
        self.waarde_in_meters = tk.StringVar()

        meters_etiket = ttk.Label(self, text="metres")
        meters_invoer = ttk.Entry(self, width=10, textvariable=self.waarde_in_meters, font=(None, 15))  # None means "don't change the font".
        voeten_etiket = ttk.Label(self, text="feet")
        voeten_tonen = ttk.Label(self, textvariable=self.waarde_in_voeten)
        bereken_knop = ttk.Button(self, text="Calculate", command=self.Methode_Bereken)

        meters_etiket.grid(column=0, row=0, sticky="W")
        meters_invoer.grid(column=1, row=0, sticky="EW")
        meters_invoer.focus()

        voeten_etiket.grid(column=0, row=1, sticky="W")
        voeten_tonen.grid(column=1, row=1, sticky="EW")

        bereken_knop.grid(column=0, row=2, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)


    def Methode_Bereken(self, *args):
        try:
            meters = float(self.waarde_in_meters.get())
            voeten = meters * 3.28084
            self.waarde_in_voeten.set(f"{voeten:.3f}")
        except ValueError:
             pass

class e_ttkFrame_Klasse_FrameScherm_VoetennaarMeters(ttk.Frame):
    def __init__(self,bewaarplek, **kwargs):
        super().__init__(bewaarplek, **kwargs)

        self.waarde_in_voeten = tk.StringVar()
        self.waarde_in_meters = tk.StringVar()

        voeten_etiket = ttk.Label(self, text="feet")
        voeten_invoer = ttk.Entry(self, width=10, textvariable=self.waarde_in_voeten, font=(None, 15))  # None means "don't change the font".
        meters_etiket = ttk.Label(self, text="meters")
        meters_tonen = ttk.Label(self, textvariable=self.waarde_in_meters)
        bereken_knop = ttk.Button(self, text="Calculate", command=self.Methode_Bereken)

        voeten_etiket.grid(column=0, row=0, sticky="W")
        voeten_invoer.grid(column=1, row=0, sticky="EW")
        voeten_invoer.focus()

        meters_etiket.grid(column=0, row=1, sticky="W")
        meters_tonen.grid(column=1, row=1, sticky="EW")


        bereken_knop.grid(column=0, row=2, columnspan=2, sticky="EW")



        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)


    def Methode_Bereken(self, *args):
        try:
            voeten = float(self.waarde_in_voeten.get())
            meters = meters / 3.28084
            self.waarde_in_meters.set(f"{meters:.3f}")
        except ValueError:
             pass


StartScherm_Object = e_tkTK_Klasse_DistanceConverterStartScherm()

font.nametofont("TkDefaultFont").configure(size=15)

StartScherm_Object.columnconfigure(0, weight=1)

StartScherm_Object.mainloop()