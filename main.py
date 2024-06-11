import tkinter as tk

calculation = ""

def addToCalculator(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)


def evaluateCalculation():
    global calculation
    print(calculation)
    try:
        
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        clearField()
        textResult.insert(1.0, "Error")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0,"end")

def deleteLastChar():
    global calculation
    calculation = calculation[:-1]
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def keyPressed(event):
    char = event.char
    if char in "0123456789+-*/()":
        addToCalculator(char)
    elif char == "\r":
        evaluateCalculation()
    elif char == "\x08":
        deleteLastChar()
    elif char == "C":
        clearField()

root = tk.Tk()
root.geometry("300x275")
textResult = tk.Text(root,height=2, width=16, font=("Arial",24))
textResult.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: addToCalculator(1), width=5, font=("Arial", 14))
btn1.grid(row=2,column=1)

btn2 = tk.Button(root, text="2", command=lambda: addToCalculator(2), width=5, font=("Arial", 14))
btn2.grid(row=2,column=2)

btn3 = tk.Button(root, text="3", command=lambda: addToCalculator(3), width=5, font=("Arial", 14))
btn3.grid(row=2,column=3)

btn4 = tk.Button(root, text="4", command=lambda: addToCalculator(4), width=5, font=("Arial", 14))
btn4.grid(row=3,column=1)

btn5 = tk.Button(root, text="5", command=lambda: addToCalculator(5), width=5, font=("Arial", 14))
btn5.grid(row=3,column=2)

btn6 = tk.Button(root, text="6", command=lambda: addToCalculator(6), width=5, font=("Arial", 14))
btn6.grid(row=3,column=3)

btn7 = tk.Button(root, text="7", command=lambda: addToCalculator(7), width=5, font=("Arial", 14))
btn7.grid(row=4,column=1)

btn8 = tk.Button(root, text="8", command=lambda: addToCalculator(8), width=5, font=("Arial", 14))
btn8.grid(row=4,column=2)

btn9 = tk.Button(root, text="9", command=lambda: addToCalculator(9), width=5, font=("Arial", 14))
btn9.grid(row=4,column=3)

btn0 = tk.Button(root, text="0", command=lambda: addToCalculator(0), width=5, font=("Arial", 14))
btn0.grid(row=5,column=2)

btnPlus = tk.Button(root, text="+",command=lambda: addToCalculator("+"), width=5,font=("Arial",14))
btnPlus.grid(row=2,column=4)


btnPlus = tk.Button(root, text="+",command=lambda: addToCalculator("+"), width=5,font=("Arial",14))
btnPlus.grid(row=2,column=4)


btnMinus = tk.Button(root, text="-",command=lambda: addToCalculator("-"), width=5,font=("Arial",14))
btnMinus.grid(row=3,column=4)


btnMul = tk.Button(root, text="*",command=lambda: addToCalculator("*"), width=5,font=("Arial",14))
btnMul.grid(row=4,column=4)

btnDiv = tk.Button(root, text="/",command=lambda: addToCalculator("/"), width=5,font=("Arial",14))
btnDiv.grid(row=5,column=4)


btnOpen = tk.Button(root, text="(",command=lambda: addToCalculator("("), width=5,font=("Arial",14))
btnOpen.grid(row=5,column=1)

btnClose = tk.Button(root, text=")",command=lambda: addToCalculator(")"), width=5,font=("Arial",14))
btnClose.grid(row=5,column=3)

btnClear = tk.Button(root, text="Clear",command=clearField, width=5,font=("Arial",14))
btnClear.grid(row=6,column=1)

btnEquals = tk.Button(root, text="=",command=evaluateCalculation, width=11,font=("Arial",14))
btnEquals.grid(row=6,column=3, columnspan=2)

btnDelete = tk.Button(root, text="Del", command=deleteLastChar, width=5, font=("Arial", 14))
btnDelete.grid(row=6,column=2)

root.bind("<Key>", keyPressed)

root.mainloop()