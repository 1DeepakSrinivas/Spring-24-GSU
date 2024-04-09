class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.num + other.num)
        else:
            raise TypeError("Other object must be of type Number")

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.num - other.num)
        else:
            raise TypeError("Other object must be of type Number")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num)
        else:
            raise TypeError("Other object must be of type Number")

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.num != 0:
                return Number(self.num // other.num)
            else:
                raise ZeroDivisionError("Cannot divide by zero")
        else:
            raise TypeError("Other object must be of type Number")


num1 = Number(25)
num2 = Number(5)

print(f'{num1} + {num2} = {str(num1 + num2)}')
print(f'{num1} - {num2} = {str(num1 - num2)}')
print(f'{num1} * {num2} = {str(num1 * num2)}')
print(f'{num1} / {num2} = {str(num1 / num2)}')

num3 = ((num1 + num2) * num1) / (num2 * num1)
print(f'({num1} + {num2}) - {num1}) * {num2 / num1} = {str(num3)}')

