def build_dictionary():
    user_input=input(':> ')
    word_frequency={}

    user_input=user_input.lower()
    words=user_input.split()
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
            word_frequency[word]=1
            
    print(f'Word List:')
    print(sorted(word_frequency.keys()),end='\n')

    print('Bag of Words:')
    for val in sorted(word_frequency.keys()):
        print(f'{val} - {word_frequency[val]}')

build_dictionary()