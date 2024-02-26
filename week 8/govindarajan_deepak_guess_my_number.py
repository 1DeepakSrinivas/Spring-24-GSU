import random
def guess_my_number():
    number = random.randint(1, 100)
    print("I have generated random number between 1 and 100. You will have 10 attempts to guess that number.")
    for i in range(0,10):
        guess=int(input(f"Guess {i+1}: "))
        if guess==number:
            print("You correctly guessed my random number!")
        elif guess<number:
            print("Your guess is lower than my random number. Try again.")
        elif guess>number:
            print("Your guess is higher than my random number. Try again.")

guess_my_number()