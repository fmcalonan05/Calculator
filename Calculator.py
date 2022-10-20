from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
frame = ttk.Frame(root, padding=10)
frame.grid()

calculationString = ""
negative_number = False

def addNumberToLabel(button):
    global calculationString
    calculationString = calculationString + button.cget('text')
    ttk.Label(frame, text=calculationString).grid(column=1, columnspan=5, row=1)

# method for appending numbers to calculator screen

# number buttons and their methods

one = ttk.Button(frame, text='1' , command=lambda: addNumberToLabel(one))
one.grid(column=1, row=2)

two = ttk.Button(frame, text='2', command=lambda: addNumberToLabel(two))
two.grid(column=2, row=2)

three = ttk.Button(frame, text='3', command=lambda: addNumberToLabel(three))
three.grid(column=3, row=2)

four = ttk.Button(frame, text='4', command=lambda: addNumberToLabel(four))
four.grid(column=1, row=3)

five = ttk.Button(frame, text='5', command=lambda: addNumberToLabel(five))
five.grid(column=2, row=3)

six = ttk.Button(frame, text='6', command=lambda: addNumberToLabel(six))
six.grid(column=3, row=3)

seven = ttk.Button(frame, text='7', command=lambda: addNumberToLabel(seven))
seven.grid(column=1, row=4)

eight = ttk.Button(frame, text='8', command=lambda: addNumberToLabel(eight))
eight.grid(column=2, row=4)

nine = ttk.Button(frame, text='9', command=lambda: addNumberToLabel(nine))
nine.grid(column=3, row=4)

zero = ttk.Button(frame, text='0', command=lambda: addNumberToLabel(zero))
zero.grid(column=2, row=5)

#operator methods for operator buttons

def operator(button):
    global calculationString
    global negative_number
    if calculationString == "" and button.cget('text') == '-':
        calculationString = calculationString + button.cget('text')
        ttk.Label(frame, text=calculationString).grid(column=1, columnspan=5, row=1)
        negative_number = True
    elif calculationString == "" and button.cget('text') != '-':
        pass
    else:
        calculationString = calculationString + button.cget('text')
        ttk.Label(frame, text=calculationString).grid(column=1, columnspan=5, row=1)


# operator buttons
add = ttk.Button(frame, text="+", command= lambda: operator(add))
add.grid(column=4, row=2)

subtract = ttk.Button(frame, text="-", command=lambda: operator(subtract))
subtract.grid(column=5, row=2)

multiply = ttk.Button(frame, text="*", command=lambda: operator(multiply))
multiply.grid(column=4, row=3)

divide = ttk.Button(frame, text="/", command=lambda: operator(divide))
divide.grid(column=5, row=3)


#equals method for calculation
def equalsFunc():
    global calculationString
    global negative_number

    if '+' in calculationString and calculationString[calculationString.index('+')+1] != None:
        numbers = calculationString.split("+")
        answer = int(numbers[0]) + int(numbers[1])
        ttk.Label(frame, text = "    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
        calculationString = ''
    elif '*' in calculationString and calculationString[calculationString.index('*')+1] != None:
        numbers = calculationString.split("*")
        answer = int(numbers[0]) * int(numbers[1])
        ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
        calculationString = ''
    elif '/' in calculationString and calculationString[calculationString.index('/')+1] != None:
        numbers = calculationString.split("/")
        answer = int(numbers[0]) / int(numbers[1])
        ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
        calculationString = ''
    else:
        if '-' in calculationString and calculationString[calculationString.index('/')+1] != None and negative_number == False:
            numbers = calculationString.split("-")
            answer = int(numbers[0])-int(numbers[1])
            ttk.Label(frame, text="    "+str(answer)+"     ").grid(column=1,columnspan=5, row = 1)
            calculationString = ''
        elif '-' in calculationString and calculationString[calculationString.index('/')+1] != None and negative_number == True:
            numbers = calculationString.lstrip().split('-')
            answer = int(numbers[0]*-1)-int(numbers[1])
            ttk.Label(frame, text="    " + str(answer) + "     ").grid(column=1, columnspan=5, row=1)
            negative_number = False
            calculationString = ''
        else:
            pass

equals = ttk.Button(frame, text="=", command = lambda:equalsFunc())
equals.grid(column=4, columnspan=2, row=4)

# main loop to run the calculator
root.mainloop()