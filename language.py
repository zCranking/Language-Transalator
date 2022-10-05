from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

root = Tk()
root.title("Language Transalator")
root.geometry("800x600")
root.config(bg="#EE6352")

title = Label(root, text="Language Transalator", bg="#EE6352", fg="#5465FF", font=("Comic Sans MS", "23", "bold"))
font = ("Consolas", 22, "normal")
title.place(relx=0.5, rely=0.1, anchor=CENTER)

text = Text(root, bg="#EE6352", font=("Comic Sans MS", "15", "bold"), height=15, wrap=WORD, width=40, padx=5, pady=5, bd=0)
text.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()