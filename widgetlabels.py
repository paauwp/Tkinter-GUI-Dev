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

# Text Label 1
label = ttk.Label(root, text="Hello World", padding=20)
label.config(font=("Segoe UI", 20))

# Picture 1
image = Image.open("logo2.png").resize((64,64))
photo = ImageTk.PhotoImage(image)
picture_text = ttk.Label(root, text="This is the text", image=photo, padding=5, compound="right")
label.pack()
picture_text.pack()

# Label with Dynamic text
text_label = tk.StringVar()
dynamic_label = ttk.Label(root, padding=10, textvariable=text_label)
dynamic_label.pack()

text_label.set("Hello John!")


root.mainloop()