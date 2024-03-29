
import tkinter as tk
from tkinter import ttk

# Set Windows 10 High DPI
try:
    from ctypes import windll
    print("Windows High DPI detected")
    windll.shcore.SetProcessDpiAwareness(1)

except:
    print("No Windows 10 High DPI detected")

def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    # If user_name is empty, print Hello, World!
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20,10,20,0))
input_frame.grid(sticky="EW")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0)
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

button_frame = ttk.Frame(root, padding=(20,10))
button_frame.grid(sticky="EW")

button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)

greet_button = ttk.Button(button_frame, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.grid(row=0,column=1, sticky="EW")

root.mainloop()