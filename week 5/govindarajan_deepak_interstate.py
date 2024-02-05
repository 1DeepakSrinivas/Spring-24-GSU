def interstate():
    hwy_no=int(input("Please enter an Interstate number: "))
    orientation=""
    if 1 <= hwy_no <= 99:
        if hwy_no % 2 == 0:
            orientation = "east/west"
        else:
            orientation = "north/south"
        print(f"Primary highway running {orientation}.")
    elif 100 <= hwy_no <= 999:
        primary_highway = hwy_no % 100
        if 1 <= primary_highway <= 99:
            if primary_highway % 2 == 0:
                orientation = "east/west"
            else:
                orientation = "north/south"
            print(f"Auxiliary highway servicing I-{primary_highway}, running {orientation}.")    
        else:
            print("Invalid auxiliary highway number.")
    else:
        print("Invalid highway number.")

interstate()