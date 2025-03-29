import tkinter
from tkinter import messagebox, ttk

root = tkinter.Tk()
root.title("Oefening 1")
root.geometry("500x600")



def open_msg():
    msg = tkinter.messagebox
    msg.showinfo("Oef 2", "Test")

btn = ttk.Button(root, text="Click me!", command=open_msg())
btn.pack(pady=20)


root.mainloop()