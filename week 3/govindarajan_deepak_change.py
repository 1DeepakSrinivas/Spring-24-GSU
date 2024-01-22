def change():
    number_cents=int(input('Please enter the number of cents: '))
    number_nickels=number_cents//5
    number_dimes=(number_cents%5)//10
    number_pennies=(number_cents%5)%10
    print(f'Coins: {number_nickels} nickels, {number_dimes} dimes, {number_pennies} pennies.')
change()