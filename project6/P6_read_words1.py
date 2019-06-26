with open('sowpods_short.txt') as f:
    lines = f.read().splitlines()
    i = 0
    while i < len(lines):
        print(lines[i])
        i += 1
    print("There are 24 words in the list")
    print("")
    #word = "dog" 
    word_list = []
    word = ""
    while word != '$':
        word = input("Type a word to find in word list, or $ to exit: ")
        word_list.append(word)
        if word in lines:
            print("found", word)
        else:
            print("did not find", word)
