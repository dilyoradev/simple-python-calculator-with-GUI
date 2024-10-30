def show(displaybox, num):
    displaybox.insert('end', num)
    
def clear(displaybox):
    displaybox.delete('1.0', 'end')
    
def assign(displaybox, sign):
    global op, num1
    op=sign
    num1=displaybox.get('1.0','end-1c')
    clear(displaybox)
    
def calculate(displaybox):
    result = 0
    num2=displaybox.get('1.0', 'end-1c')
    
    if op=='+':
        result = float(num1) + float(num2)
    elif op=='-':
        result = float(num1) - float(num2)
    elif op=='*':
        result = float(num1) * float(num2)
    elif op=='/':
        result= float(num1) / float(num2)    
    clear(displaybox)
    displaybox.insert('end', result)
   