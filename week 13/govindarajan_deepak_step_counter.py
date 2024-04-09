class NegativeValueError(Exception):
    pass

def steps_to_miles(steps):
    try:
        steps = int(steps)
        if steps < 0:
            raise NegativeValueError("Exception: Negative Step Count Entered.")
        return steps / 2000
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")

def main():
    try:
        steps = input("Enter the number of steps: ")
        miles = steps_to_miles(steps)
        print(f'{miles:.2f} miles')
    except (ValueError, NegativeValueError) as e:
        print(e)

main()