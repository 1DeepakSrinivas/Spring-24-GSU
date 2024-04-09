class Number:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        try:
            return Number(self.num + other.num)
        except AttributeError:
            raise TypeError("Other object must be of type Number")

    def __sub__(self, other):
        try:
            return Number(self.num - other.num)
        except AttributeError:
            raise TypeError("Other object must be of type Number")

    def __mul__(self, other):
        try:
            return Number(self.num * other.num)
        except AttributeError:
            raise TypeError("Other object must be of type Number")

    def __truediv__(self, other):
        try:
            if other.num != 0:
                return Number(self.num // other.num)
            else:
                raise ZeroDivisionError("Cannot divide by zero")
        except AttributeError:
            raise TypeError("Other object must be of type Number")

num1 = Number(25)
num2 = Number(5)

result_add = num1 + num2
print(f"{num1} + {num2} = {result_add}")

result_sub = num1 - num2
print(f"{num1} - {num2} = {result_sub}")

result_mul = num1 * num2
print(f"{num1} * {num2} = {result_mul}")

result_div = num1 / num2
print(f"{num1} / {num2} = {result_div}")

result_comb=(result_add+result_sub*result_div)/result_mul
print(f"({result_add} + {result_sub} * {result_div}) / {result_mul} = {result_comb}")

