'''def text_filter():
    input_message=input("Enter your message: ")
    output_message=[]
    banned_words=['turkey','dog','fox','cat','chicken']
    words=input_message.split()
    for word in words:
        if word.lower() not in banned_words:
            output_message.append(word)
            
    print(f"Input Message: {input_message}")
    print(f"Output Message: {output_message.join()}")

text_filter()
'''

def text_filter():
    input_message = input("Enter your message: ")
    output_message = []
    banned_words = ['turkey', 'dog', 'fox', 'cat', 'chicken']
    words = input_message.split()
    for word in words:
        if word.lower() not in banned_words:
            output_message.append(word)
            
    print(f"Input Message: {input_message}")
    print(f"Output Message: {' '.join(output_message)}")

text_filter()

