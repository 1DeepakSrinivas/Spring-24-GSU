import math
def calculator():
    while True:
        print("Please enter an expression")
        expression = input(":> ")
        
        add_split=expression.split(sep='+')
        sub_split=expression.split(sep='-')
        mul_split=expression.split(sep='*')
        div_split=expression.split(sep='/')
        mod_split=expression.split(sep='%')
        exp_split=expression.split(sep='**')
        floor_split=expression.split(sep='//')

        if '+' in expression:
            addition(add_split[0],add_split[1])
        if '-' in expression:
            subtraction(sub_split[0],sub_split[1])
        if '*' in expression:
            multiplication(mul_split[0],mul_split[1])
        if '/' in expression:
            division(div_split[0],div_split[1])
        if '%' in expression:
            modulus(mod_split[0],mod_split[1])
        if '**' in expression:
            exponent(exp_split[0],exp_split[1])
        if '//' in expression:
            floor_division(floor_split[0],floor_split[1])
        if expression.lower() == 'exit' or 'quit' or 'q':
            break
        elif len(expression)<3:
            print("Invalid expression")
    
def addition(a,b):
    print(f'Result: {a}+{b} = {int(a)+int(b)}')

def subtraction(a,b):
    print(f'Result: {a}-{b} = {int(a)-int(b)}')

def multiplication(a,b):
    print(f'Result: {a}*{b} = {int(a)*int(b)}')

def division(a,b):
    print(f'Result: {a}/{b} = {int(a)/int(b)}')

def modulus(a,b):
    print(f'Result: {a}%{b} = {int(a)%int(b)}')

def exponent(a,b):
    print(f'Result: {a}**{b} = {math.pow(int(a),int(b))}')

def floor_division(a,b):
    print(f'Result: {a}//{b} = {int(a)//int(b)}')
    
calculator()
    