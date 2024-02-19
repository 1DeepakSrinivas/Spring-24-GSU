def reverse():
    while True:
        text = input("Please enter your string: ")
        if text.lower() in ['quit', 'q']:
            break
        reversed_text = ''
        for i in range(len(text) - 1, -1, -1):
            reversed_text += text[i]
        print(reversed_text)

reverse()