def scrabble():
    letter_points={'a':1,
                   'b':3,
                   'c':3,
                   'd':2,
                   'e':1,
                   'f':4,
                   'g':2,
                   'h':4,
                   'i':1,
                   'j':8,
                   'k':5,
                   'l':1,
                   'm':3,
                   'n':1,
                   'o':1,
                   'p':3,
                   'q':10,
                   'r':1,
                   's':1,
                   't':1,
                   'u':1,
                   'v':4,
                   'w':4,
                   'x':8,
                   'y':4,
                   'z':10}
    while True:
        user_input=input(":> ")
        score=0
        user_input=user_input.lower()
        if user_input in ['exit','quit','q','e']:
            break
        for letter in user_input:
            score+=letter_points[letter]
        print(f'{user_input.upper()} is worth {score} points.')
        if user_input in ['exit','quit','q','e']:
            break


scrabble()
    