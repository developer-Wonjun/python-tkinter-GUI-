from tkinter import *
import random

answer = random.randint(1, 100)
n = 0
def guessing():
    
    guess = int(guessingEntry.get())
    global n
    if guess > answer:
        n += 1
        msg = "좀 낮춰봐~!"
        
    elif guess < answer:
        n += 1
        msg = "좀 높여봐~!!"
    else:
        msg = "정답!"
    
    result["text"] = msg
    guessingEntry.delete(0, 5)

    if n == 7:
        msg = "횟수 초과! 실패!!! 정답은 : " + str(answer)
        result["text"] = msg
 
def reset():
    global answer
    global n
    answer = random.randint(1,100)
    n = 0
    result["text"] = "처음부터 다시 ~!"




window = Tk()
window.title("숫자게임")
Label(window, text="원준's 숫자 게임에 오신 것을 환영합니다.").pack()

guessingEntry = Entry(window)
guessingEntry.pack(side="left")

trybutton = Button(window, text="시도", fg="green", command=guessing)
trybutton.pack(side="left")

resetbutton = Button(window, text="초기화", fg="red", command=reset)
resetbutton.pack(side="left")

result = Label(window, text = "1부터 100 사이의 정수를 입력하세요!")
result.pack(side="left")


window.mainloop()