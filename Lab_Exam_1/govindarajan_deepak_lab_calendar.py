''' To create a program that will determine the season
    based on the input day and month of the year in the southern hemisphere.'''

def calendar_south_hem():
    user_month=input("Please enter the month:")
    user_day=int(input("Please enter the day:"))

    autumn_months=['march','april','may','june']
    winter_months=['june','july','august','september']
    spring_months=['september','october','november','december']
    summer_months=['december','january','february','march']

    is_autumn=False
    is_winter=False
    is_spring=False
    is_summer=False

    user_month=user_month.lower()

    if user_month in autumn_months:
        is_autumn=True
        if is_autumn==True:
            if user_month=='march' and user_day>=21:
                print(f'{user_month.title()} {user_day} is Autumn in the southern hemisphere.')
            else:
                print(f'{user_month.title()} {user_day} is Summer in the southern hemisphere.')

    if user_month in winter_months:
        is_winter=True
        if is_winter==True:
            if user_month=='june' and user_day>=21:
                print(f'{user_month.title()} {user_day} is Winter in the southern hemisphere.')
            else:
                print(f'{user_month.title()} {user_day} is Autumn in the southern hemisphere.')

    if user_month in spring_months:
        is_spring==True
        if is_spring==True:
            if user_month=='september'and user_day>=21:
                print(f'{user_month.title()} {user_day} is Spring in the southern hemisphere.')
            else:
                print(f'{user_month.title()} {user_day} is Winter in the southern hemisphere.')

    if user_month in summer_months:
        is_summer=True
        if is_summer==True:
            if user_month=='december' and user_day>=21:
                print(f'{user_month.title()} {user_day} is Summer in the southern hemisphere.')
            else:
                print(f'{user_month.title()} {user_day} is Spring in the southern hemisphere.')

calendar_south_hem()