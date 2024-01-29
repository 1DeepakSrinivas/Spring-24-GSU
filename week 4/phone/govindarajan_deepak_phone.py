def ph_format():
    phone_num =int(input("Please enter your phone number: "))
    if phone_num<1000000000:
        print("Invalid phone number. Please enter a valid Phone Number")
        ph_format()
    area_code = phone_num // 10000000
    prefix = (phone_num % 10000000) // 10000
    line_number = phone_num % 10000
    print(f"({area_code}) {prefix}-{line_number}")

ph_format()