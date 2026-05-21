exp = input("expression: ")
x,operator,y = exp.split()
x = float(x)
y = float(y)

def maths(x,operator,y):
    if operator == '+':
        print(x+y)
    elif operator == '-':
        print(x-y)
    elif operator == '*':
        print(x*y)
    elif operator == '/':
        print(x/y)
    else:
        print("operator not available")


maths(x,operator,y)


    
