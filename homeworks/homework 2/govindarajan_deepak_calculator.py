def calculator():
    while True:
        print("Please enter an expression")
        expression = input(":> ")
        split_exp=expression.split()
        
        if '+' in split_exp:
            addition(split_exp[0],split_exp[2])
        elif '-' in split_exp:
            subtraction(split_exp[0],split_exp[2])
        elif '*' in split_exp:
            multiplication(split_exp[0],split_exp[2])
        elif '/' in split_exp:
            division(split_exp[0],split_exp[2])
        elif '%' in split_exp:
            modulus(split_exp[0],split_exp[2])
        elif '**' in split_exp:
            exponent(split_exp[0],split_exp[2])
        elif '//' in split_exp:
            floor_division(split_exp[0],split_exp[2])
        elif expression.lower() == 'exit' or 'quit' or 'q':
            break

        else:
            print("Invalid expression")
    
def addition(a,b):
    print(a+b)

def subtraction(a,b):
    print(a-b)

def multiplication(a,b):
    print(a*b)

def division(a,b):
    print(a/b)

def modulus(a,b):
    print(a%b)

def exponent(a,b):
    print(a**b)

def floor_division(a,b):
    print(a//b)
    
calculator()
    