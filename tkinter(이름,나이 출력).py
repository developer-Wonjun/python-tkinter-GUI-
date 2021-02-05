from tkinter import *


window = Tk()

def show():
    print("%s, %s" % (e1.get(), e2.get()))

Label(window, text = "이름").grid(row=0, column=1)
Label(window, text="나이").grid(row=1, column=1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

Button(window, text="종료", command=window.quit).grid(row=3, column=1, sticky=W, padx = 10, pady = 10)
Button(window, text="보이기", command = show).grid(row=3, column=3, sticky =W, padx=10, pady=10)

window.mainloop()