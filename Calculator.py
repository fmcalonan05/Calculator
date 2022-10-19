from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
frame = ttk.Frame(root, padding=10)
frame.grid()
#creating root and frame tkinter application
firstNumberBool = True
firstNumber = ''
secondNumberBool = False
secondNumber = ''
#variables to track numbers in calculator
addBool = False
subtractBool = False
multiplyBool = False
divideBool = False
#variables to track the operator

ttk.Label(frame, text="").grid(column=1,columnspan=5, row = 1)
#calculator screen initialisation

def addNumberToLabel(button):
    if firstNumberBool:
        global firstNumber
        firstNumber = firstNumber + button.cget('text')
        ttk.Label(frame, text=firstNumber).grid(column=1,columnspan=5, row = 1)
    else:
        global secondNumber
        firstNumber = firstNumber+ secondNumber + button.cget('text')
        ttk.Label(frame, text=firstNumber).grid(column=1, columnspan=5, row=1)
#method for appending numbers to calculator screen

#number buttons and their methods
one = ttk.Button(frame, text='1' ,command = lambda: addNumberToLabel(one))
one.grid(column=1, row=2)

two = ttk.Button(frame, text='2',command = lambda: addNumberToLabel(two))
two.grid(column=2, row=2)

three = ttk.Button(frame, text='3',command = lambda: addNumberToLabel(three))
three.grid(column=3, row=2)

four = ttk.Button(frame, text='4',command = lambda: addNumberToLabel(four))
four.grid(column=1, row=3)

five = ttk.Button(frame, text='5',command = lambda: addNumberToLabel(five))
five.grid(column=2, row=3)

six = ttk.Button(frame, text='6',command = lambda: addNumberToLabel(six))
six.grid(column=3, row=3)

seven = ttk.Button(frame, text='7',command = lambda: addNumberToLabel(seven))
seven.grid(column=1, row=4)

eight = ttk.Button(frame, text='8',command = lambda: addNumberToLabel(eight))
eight.grid(column=2, row=4)

nine = ttk.Button(frame, text='9',command = lambda: addNumberToLabel(nine))
nine.grid(column=3, row=4)

zero = ttk.Button(frame, text = '0', command = lambda: addNumberToLabel(zero))
zero.grid(column = 2, row=5)

#operator methods for operator buttons

def operator(button):
    global firstNumberBool
    if firstNumberBool:
        firstNumberBool = False
        global firstNumber
        firstNumber = (firstNumber) + button.cget('text')
        ttk.Label(frame, text=firstNumber).grid(column=1,columnspan=5, row = 1)
        global secondNumberBool
        secondNumberBool = True
        if button.cget('text') == '+':
            global addBool
            addBool= True
        if button.cget('text') == '-':
            global subtractBool
            subtractBool = True
        if button.cget('text') == '*':
            global multiplyBool
            multiplyBool= True
        if button.cget('text') == '/':
            global divideBool
            divideBool= True


#operator buttons
add = ttk.Button(frame, text="+",command= lambda: operator(add))
add.grid(column=4, row=2)

subtract = ttk.Button(frame, text="-",command=lambda: operator(subtract))
subtract.grid(column=5, row=2)

multiply = ttk.Button(frame, text="*",command=lambda: operator(multiply))
multiply.grid(column=4, row=3)

divide = ttk.Button(frame, text="/",command=lambda: operator(divide))
divide.grid(column=5, row=3)


#equals method for calculation
def equalsFunc():
    global firstNumber
    global secondNumber
    global firstNumberBool
    global secondNumberBool
    global addBool
    global subtractBool
    global multiplyBool
    global divideBool

    if addBool and secondNumberBool:
        numbers = firstNumber.split("+")
        answer = int(numbers[0]) + int(numbers[1])
        ttk.Label(frame, text = "    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
    elif subtractBool and secondNumberBool:
        numbers = firstNumber.split("-")
        answer = int(numbers[0]) - int(numbers[1])
        ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
    elif multiplyBool and secondNumberBool:
        numbers = firstNumber.split("*")
        answer = int(numbers[0]) * int(numbers[1])
        ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
    else:
        numbers = firstNumber.split("/")
        answer = int(numbers[0])/int(numbers[1])
        ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)


    firstNumber = ""
    secondNumber =""
    firstNumberBool= True
    secondNumberBool= False
    addBool = False
    subtractBool = False
    multiplyBool = False
    divideBool = False

#equals button

equals = ttk.Button(frame, text="=", command = lambda:equalsFunc())
equals.grid(column=4, columnspan=2, row=4)


#main loop to run the calculator
root.mainloop()