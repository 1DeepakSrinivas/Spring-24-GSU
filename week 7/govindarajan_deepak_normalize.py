def normalize():
    num=int(input("Please enter the number of floating-point values:"))
    float_nums=[]
    for i in range(num):
        float_num=float(input("Please enter a floating-point value:"))

        float_nums.append(float_num)
    
    print('Normalized Floating Point Values:')
    for num in float_nums:
        print(f'{num:.2f}')

normalize()
        