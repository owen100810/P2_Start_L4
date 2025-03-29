import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("300x200")
frame = tkinter.Frame()
label_naam = tkinter.Label(text="Voer een Pokémon-naam in:")
label_naam.grid(row=0, column=1)
label_naam.place(anchor= label_naam.CENTER)

root.mainloop()