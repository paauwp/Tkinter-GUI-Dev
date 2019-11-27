import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class DistanceConverter(tk.Tk):
    def __init___(self):
        super.__init__(self)

        self.title("Distance Converter")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=(60,30))
        frame.grid()



#root.geometry("300x150")


font.nametofont("TkDefaultFont").configure(size=15)

nm_value = tk.StringVar()
km_value = tk.StringVar(value = "Km's shown here")

def calculate_metres(*args):
    try:
        nm = float(nm_value.get())
        metres = nm * 1.85200
        km_value.set(f"{metres:.3f}")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

#--Widgets--
nm_label = ttk.Label(main, text="Nm:")
nm_input = ttk.Entry(main, width=10, textvariable=nm_value, font=("Segoe UI",15))
metres_label = ttk.Label(main, text="Km:")
metres_display = ttk.Label(main, textvariable=km_value)
calc_button= ttk.Button(main, text="Calculate", command=calculate_metres)

# --Placing the labels in a grid--
nm_label.grid(column=0, row=0, sticky="EW")
nm_input.grid(column=1, row=0, sticky="EW")
nm_input.focus()
metres_label.grid(column=0, row=1, sticky="EW")
metres_display.grid(column=1, row=1, sticky="EW")
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

# Keybindings
root.bind("<Return>", calculate_metres)
root.bind("<KP_Enter>", calculate_metres)

root.mainloop()