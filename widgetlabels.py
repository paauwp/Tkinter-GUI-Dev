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
root.title("Widget Examples")

label = ttk.Label(root, text="Hello World", padding=20)
label.config(font=("Segoe UI", 20))
image = Image.open("logo2.png")
photo = ImageTk.PhotoImage(image)
label2 = ttk.Label(root, image=photo, padding=20)
label.pack()
label2.pack()

root.mainloop()