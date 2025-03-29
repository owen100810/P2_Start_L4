import tkinter as tk
from tkinter import colorchooser

def kies_kleur():
    global kleur
    kleur = colorchooser.askcolor()[1]
    knop.config(bg=kleur)

def teken(e):
    canvas.create_line(e.x -3, e.y -3, e.x+3, e.y+3, fill=kleur, width=5)

root = tk.Tk()
root.title("Kleur")
kleur = "black"
knop = tk.Button(root, text="Kies een kleur", command=kies_kleur)
knop.pack()
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", teken)
root.mainloop()