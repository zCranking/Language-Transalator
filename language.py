from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator

root = Tk()
root.title("Language Transalator")
root.geometry("800x600")
root.config(bg="#EE6352")

title = Label(root, text="Language Transalator", bg="#EE6352", fg="#5465FF", font=("Comic Sans MS", "23", "bold"))
title.place(relx=0.5, rely=0.1, anchor=CENTER)

text = Text(root, font=("Consolas", 22, "normal"), height=15, wrap=WORD, width=40, padx=5, pady=5, bd=0)
text.place(relx=0.5, rely=0.65, anchor=CENTER)

Thelist = list(LANGUAGES.values())
languages = ttk.Combobox(state=readonly, values=Thelist[1], width=6)
languages.place(relx=0.2, rely=0.5, anchor=CENTER)
languages.set("english")

Output = Label(root, text="Output", bg="#EE6352", font=("Consolas", 22, "normal"))
Output.place(relx=0.7, rely=0.5, anchor=CENTER)


root.mainloop()