from tkinter import *
from math import *

def calculate(event):
    label["text"] = str(eval(entry.get()))
    #label.configure(text="계산결과 :" + str(eval(entry.get())))
window = Tk()
Label(window, text="원준이 계산기").pack() 

entry = Entry(window)
entry.bind("<Return>", calculate)
entry.pack()

label = Label(window, text="계산결과 : ")
label.pack()

window.mainloop()
