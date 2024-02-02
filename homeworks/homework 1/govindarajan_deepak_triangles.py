import math as m

def triangles():
    is_right_angled=False
    is_acute_angled=False
    is_obtuse_angled=False
    
    side_a=int(input("Please enter the length of side A (in metres): "))
    side_b=int(input("Please enter the length of side B (in metres): "))
    side_c=int(input("Please enter the length of side C (in metres): "))

    perimeter_triangle=side_a+side_b+side_c 
    semi_perimeter=perimeter_triangle/2

    area_triangle=m.sqrt(semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c)) #Heron's formula for area of triangle

    if (side_a**2+side_b**2==side_c**2 or 
        side_a**2+side_c**2==side_b**2 or 
        side_b**2+side_c**2==side_a**2): #Pythagorean theorem to check if right-angled
        is_right_angled=True
    elif (side_a**2+side_b**2>side_c**2 and
          side_a**2+side_c**2>side_b**2 and 
          side_b**2+side_c**2>side_a**2): #Cosine rule to check if acute-angled
        is_acute_angled=True
    elif (side_a**2+side_b**2<side_c**2 or
          side_a**2+side_c**2<side_b**2 or
           side_b**2+side_c**2<side_a**2): # to check if obtuse-angled
        is_obtuse_angled=True
    else:
        print("The triangle is invalid.")

    print(f"The perimeter of the triangle is {perimeter_triangle} metres.")
    print(f'The area of the triangle is {area_triangle:.2f} square metres.')
    if is_right_angled:
        print("The triangle is a right-angled triangle.")
    if is_acute_angled:
        print("The triangle is an acute-angled triangle.")
    if is_obtuse_angled:
        print("The triangle is an obtuse-angled triangle.")
    
triangles()

