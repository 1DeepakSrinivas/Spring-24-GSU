class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self):


def main():
    try:
        user_num = int(input(':> '))
        div_num = int(input(':> '))
        result = user_num / div_num
        print(result)
    except ValueError:
        print('Error: Input must be a number.')
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
