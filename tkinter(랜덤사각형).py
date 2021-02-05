from tkinter import *
from random import *
color =["red","orange","yellow","green","blue","violet"]
def create():
    a = randint(0, 300)
    b = randint(0, 250)
    c = randint(300, 500)
    d = randint(250, 400)

    create = w.create_rectangle(a,b,c,d, fill = choice(color))

    return create

window = Tk()
w = Canvas(window, width=500, height=400)
w.pack()

for i in range(10):
    create()

window.mainloop()

