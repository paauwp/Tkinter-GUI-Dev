import tkinter as tk
from tkinter import ttk
# from windows import set_dpi_awareness
from PIL import Image, ImageTk

# Set Windows 10 High DPI
try:
    from ctypes import windll
    print("Windows High DPI detected")
    windll.shcore.SetProcessDpiAwareness(1)

except:
    print("No Windows 10 High DPI detected")

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("Widget Examples- Tkinter Text")

# Tkinter Text Widget
text = tk.Text(root, height=8)
text.pack()
text.focus() #this give the window focus so you can input directly

text.insert("2.0", "Please enter a comment....: ")
text["state"] = "normal" # "disable" will disable the ability to give in text
text_content = text.get("1.0", "end")
print(text_content) #this will only print "Pleae enter a comment"

root.mainloop()