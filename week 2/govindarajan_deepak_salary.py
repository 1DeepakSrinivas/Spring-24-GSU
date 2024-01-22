def salary():
    hourly_wage=int(input('Please enter your hourly wage: '))
    hours_worked=int(input('Please enter the number of hours worked per week: '))
    weeks_worked=int(input('Please enter the number of weeks worked this year: '))
    print(f'Your salary so far this year is ${hourly_wage*hours_worked*weeks_worked}.')
salary()