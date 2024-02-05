def speeding_fines():
    speed_limit=int(input("Please enter the speed limit for the road: "))
    user_speed=int(input("Please enter the vehicle's recorded speed: "))
    fine=0
    if user_speed <= (speed_limit - 10):
        fine=50
    elif (user_speed >= speed_limit + 6) and (user_speed <= speed_limit + 20):
        fine=75
    elif (user_speed >= speed_limit + 21) and (user_speed <= speed_limit + 40):
        fine=150
    elif user_speed > (speed_limit + 40):
        fine=300
    else:
        fine=0

    if fine>1:
        print(f"The speeding fine is ${fine}")
    else:
        print("There is no fine.")

speeding_fines()
