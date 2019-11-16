import tkinter as tk

root = tk.Tk()
root.geometry("600x400")


rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10, fill="y", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10, ipady=10)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="red", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both")


root.mainloop()
