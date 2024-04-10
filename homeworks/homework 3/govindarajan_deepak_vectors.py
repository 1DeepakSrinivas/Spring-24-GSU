class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        try:
            new_vector=(self.x + other.x, self.y + other.y, self.z + other.z)
            return new_vector
        except AttributeError:
            raise TypeError("Other object must be of type Vector")

Vector1=Vector(1,2,3)
Vector2=Vector(4,5,6)
print(Vector.__add__(Vector1, Vector2))

def main():
    try:
        user_num = int(input(':> '))
        div_num = int(input(':> '))
        result = user_num / div_num
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

main()