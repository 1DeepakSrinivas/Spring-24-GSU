def intro():
    user_name = input("Please enter your name: ")
    class_days=str(input("Please enter the days of the week you have class: "))
    class_time=str(input("Please enter the time of day you have class: "))
    lab_days=str(input("Please enter the days of the week you have lab: "))
    lab_time=str(input("Please enter the time of day you have lab: "))

    print(f'Hello {user_name}!')
    print('Welcome to the CSC/DSCI 1301 Principles of Computer/Data Science Course!')
    print(f'Our class is held every {class_days} at {class_time}.')
    print(f'Our lab is held every {lab_days} at {lab_time}.')

intro()
