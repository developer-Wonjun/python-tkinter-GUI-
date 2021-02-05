from tkinter import *

def checked(i):
    global player
    button = list[i]

    if button["text"] != "       ":
        return
    button["text"] ="       " +player+ "       "
    button["bg"] = "yellow"
    if player == "X":
        player = "O"
        button["bg"] = "yellow"
    else :
        player = "X"
        button["bg"] = "lightgreen"
window = Tk()
player="X"
list=[]

for i in range(9):
    b = Button(window, text="       ", command=lambda k=i : checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)

window.mainloop()