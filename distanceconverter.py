import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry("600x400")
# root.resizable(False,False)
root.title("Distance Converter")

main = ttk.Frame(root, padding = (30,15))
main.grid()

root.columnconfigure(0, weight=1)

nm_value = tk.StringVar()

nm_label = ttk.Label(main, text="Nm:")
nm_input = ttk.Entry(main, width=10, textvariable=nm_value)

metres_label = ttk.Label(main, text="Meter:")
metres_display = ttk.Label(main, text="Meters shown here")
calc_button= ttk.Button(main, text="Calculate")

nm_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
nm_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
nm_input.focus()

metres_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
metres_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()