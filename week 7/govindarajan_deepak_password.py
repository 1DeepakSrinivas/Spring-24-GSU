def password():
    user_password=input("Please enter your password: ")
    replacements = {'o': '0', 'i': '1', 'a': '@', 'e': '3', 'A': '4', 'B': '8', 's': '$'}
    strong_pass = ''
    
    for char in user_password:
        if char in replacements:
            strong_pass+= replacements[char]
        else:
            strong_pass += char

    strong_pass += '!'

    print(f'Your new strong password is {strong_pass}')

password()
