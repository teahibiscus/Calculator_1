from tkinter import *

m=Tk()

m.title("Calculator")
# ADD WIDGETS HERE

frame = Frame(m)
frame.pack()

expression = ''
equation = StringVar()



#making expression


def press(num):
    global expression

    expression += str(num)
    equation.set(expression)

def equalpress():
    
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = total

def clear():
    global expression
    expression = ""
    equation.set("")




# making buttons
button1 = Button(frame, text='1', width=25, command=lambda: press(1)) 
button2 = Button(frame, text='2', width=25, command=lambda: press(2)) 
button3 = Button(frame, text='3', width=25, command=lambda: press(3)) 
button4 = Button(frame, text='4', width=25, command=lambda: press(4)) 
button5 = Button(frame, text='5', width=25, command=lambda: press(5)) 
button6 = Button(frame, text='6', width=25, command=lambda: press(6)) 
button7 = Button(frame, text='7', width=25, command=lambda: press(7)) 
button8 = Button(frame, text='8', width=25, command=lambda: press(8)) 
button9 = Button(frame, text='9', width=25, command=lambda: press(9)) 
button0 = Button(frame, text='0', width=25, command=lambda: press(0))
button_multiply = Button(frame, text = 'x', width=25, command=lambda: press("*")) 
button_add = Button(frame, text = '+', width=25, command=lambda: press("+"))
button_subtract = Button(frame, text = '-', width=25, command=lambda: press("-"))
button_divide = Button(frame, text = '/', width=25, command=lambda: press("/"))
button_equal = Button(frame, text = '=', width=25, command=lambda: equalpress())
button_clear = Button(frame, text = 'CLEAR', width=25, command = lambda: clear())
button_decimal = Button(frame, text = '.', width=25, command = lambda: press("."))
display = Entry(frame, textvariable=equation)

#setting the buttons in the frame
button1.grid(row = 3, column = 1)
button2.grid(row = 3, column = 2)
button3.grid(row = 3, column = 3)
button4.grid(row = 2, column = 1)
button5.grid(row = 2, column = 2)
button6.grid(row = 2, column = 3)
button7.grid(row = 1, column = 1)
button8.grid(row = 1, column = 2)
button9.grid(row = 1, column = 3)
button0.grid(row = 4, column = 2)
button_decimal.grid(row = 4, column = 1)
button_multiply.grid(row = 3, column = 4)
button_add.grid(row = 1, column = 4)
button_subtract.grid(row = 2, column = 4)
button_divide.grid(row = 4, column = 4)
button_equal.grid(row = 4, column = 3)
button_clear.grid(row = 5, columnspan = 5)
display.grid(row = 0, columnspan = 4, ipadx = 70)





m.mainloop()