import tkinter as tk
from logic import assign, clear, calculate, show
from settings import buttonfont
def setup_ui(window):
    
    #rootframe
    rootframe=tk.Frame(window)
    rootframe.pack()
    #the layout
    displayframe=tk.LabelFrame(rootframe, width=420, height=80)
    displayframe.grid(row=0, column=0, pady=(10,10))
    displayframe.grid_propagate(0)

    keypadframe=tk.LabelFrame(rootframe, width=420, height=450)
    keypadframe.grid(row=1, column=0, padx=10, pady=(10,10))
    keypadframe.grid_propagate(0)

    numbersframe=tk.LabelFrame(keypadframe, width=280,height=400)
    numbersframe.grid(row=0, column=0, padx=(10, 20), pady=(10,10))
    numbersframe.grid_propagate(0)

    signframe=tk.LabelFrame(keypadframe, width=100, height=400)
    signframe.grid(row=0, column=1, pady=(10, 10))
    signframe.grid_propagate(0)

    # The screen
    displaybox=tk.Text(displayframe, width=20, height=1, font=('Helvetice', 30))
    displaybox.grid(row=0, column=0, padx=(20,5), pady=(20,5))

    # numbers button
    numbers=[('1',0,0), ('2',0,1), ('3',0,2), ('4',1,0),('5',1,1), ('6',1,2), ('7',2,0), ('8',2,1),('9',2,2),('0',3,0)]
    
    
    for (text, row, col) in numbers:
            button=tk.Button(numbersframe, text=text, height=3, width=3, font=buttonfont, command=lambda num=text:show(displaybox, num))
            button.grid(row=row, column=col, padx=10,pady=10)

            
        #clear and equal buttons
    buttonce=tk.Button(numbersframe, text='CE', height=3, width=3, font=buttonfont, command=lambda:clear(displaybox))
    buttonce.grid(row=3, column=1, padx=10, pady=10)

    buttonequal=tk.Button(numbersframe, text='=', height=3, width=3, font=buttonfont, command=lambda : calculate(displaybox))
    buttonequal.grid(row=3, column=2, padx=10, pady=10)

        # operator buttons
    operators=[('+',0),('-',1),('*',2),('/',3)]

    for (op, row) in operators:
            button=tk.Button(signframe, text=op, height=3, width=3, font=buttonfont, command=lambda sign=op: assign(displaybox, sign) )
            button.grid(row=row, column=0, padx=(10,10), pady=10)

    