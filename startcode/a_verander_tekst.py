import tkinter

root = tkinter.Tk()
root.title("GUI les")
root.geometry("300x200")

# label maken
label = tkinter.Label(root, text="Welkom bij mijn eerste GUI!")
label.pack()

# Functie om tekst van label aan te passen
def verander_tekst():
    label.config(text="Welkom bij mijn eerste GUI!")

def verander_weeral():
    label.config(text="Test")

# Knop aanmaken
button = tkinter.Button(root, text="Klik op mij!", command=verander_tekst)
button1 = tkinter.Button(root, text="reset", command=verander_weeral)


button.pack()

root.mainloop()