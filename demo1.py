from tkinter import *

op = 0
v1 = 0
opFlag = True
def setLabText(num):
    if int(lab['text']) != 0 and opFlag ==False:
        lab["text"] = lab["text"] + num
    else:
        lab["text"] = num

def opSet(opValue):
    global op
    global v1
    global opFlag
    opFlag = True
    v1 = int(lab["text"])
    op = opValue

def compute():
    v2 = int(lab["text"])
    global op
    if op == 1:
        lab["text"] = v1+v2
    elif op == 2:
        lab["text"] = v1-v2
    elif op == 3:
        lab["text"] = v1*v2
    elif op == 4:
        lab["text"] = v1//v2



win = Tk()
win.geometry("400x400+200+100")
win.title =("Digital Keyboard")
win.config(bg="skyblue")

win.rowconfigure(1, weight=1)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=1)
win.rowconfigure(4, weight=1)
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
win.columnconfigure(3, weight=1)

lab = Label(win, text="0", justify=RIGHT, anchor=E, font=("Monaco", 26, "bold"), bg="#ccddee")
lab.grid(row=0, column=0, columnspan=4, sticky=EW)

btn7 = Button(win, text="7", font=("Monaco", 30, "bold"), command=lambda:setLabText('7'))
btn7.grid(row=1, column=0, sticky=NSEW)
btn8 = Button(win, text="8", font=("Monaco", 30, "bold"), command=lambda:setLabText('8'))
btn8.grid(row=1, column=1, sticky=NSEW)
btn9 = Button(win, text="9", font=("Monaco", 30, "bold"), command=lambda:setLabText('9'))
btn9.grid(row=1, column=2, sticky=NSEW)
btnDiv = Button(win, text="//", font=("Monaco", 30, "bold"), command=lambda:opSet(4))
btnDiv.grid(row=1, column=3, sticky=NSEW)

btn4 = Button(win, text="4", font=("Monaco", 30, "bold"), command=lambda:setLabText('4'))
btn4.grid(row=2, column=0, sticky=NSEW)
btn5 = Button(win, text="5", font=("Monaco", 30, "bold"), command=lambda:setLabText('5'))
btn5.grid(row=2, column=1, sticky=NSEW)
btn6 = Button(win, text="6", font=("Monaco", 30, "bold"), command=lambda:setLabText('6'))
btn6.grid(row=2, column=2, sticky=NSEW)
btnMulti = Button(win, text="*", font=("Monaco", 30, "bold"), command=lambda:opSet(3))
btnMulti.grid(row=2, column=3, sticky=NSEW)

btn1 = Button(win, text="1", font=("Monaco", 30, "bold"), command=lambda:setLabText('1'))
btn1.grid(row=3, column=0, sticky=NSEW)
btn2 = Button(win, text="2", font=("Monaco", 30, "bold"), command=lambda:setLabText('2'))
btn2.grid(row=3, column=1, sticky=NSEW)
btn3 = Button(win, text="3", font=("Monaco", 30, "bold"), command=lambda:setLabText('3'))
btn3.grid(row=3, column=2, sticky=NSEW)
btnSub = Button(win, text="-", font=("Monaco", 30, "bold"), command=lambda:opSet(2))
btnSub.grid(row=3, column=3, sticky=NSEW)


btn0 = Button(win, text="0", font=("Monaco", 30, "bold"), command=lambda:setLabText('0'))
btn0.grid(row=4, column=0, sticky=NSEW)
btnDot = Button(win, text=".", font=("Monaco", 30, "bold"), command=lambda:setLabText('.'))
btnDot.grid(row=4, column=1, sticky=NSEW)
btnEq = Button(win, text="=", font=("Monaco", 30, "bold"), command=compute)
btnEq.grid(row=4, column=2, sticky=NSEW)
btnAdd = Button(win, text="+", font=("Monaco", 30, "bold"), command=lambda:opSet(1))
btnAdd.grid(row=4, column=3, sticky=NSEW)









win.mainloop()
