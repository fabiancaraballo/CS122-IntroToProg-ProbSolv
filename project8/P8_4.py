# P8_4.py

# Display options, do the right thing, repeat

def get_option(my_codes, my_descriptions):
    ''' Display codes and descriptions from lists
        Ask user to choose a code
        Return user choice as single lower-case character
    '''
    for count in range(len(my_codes)):
        print(my_codes[count], my_descriptions[count])

    answer = input("Type your choice: ")
    option = answer[0].lower()
    for code in my_codes:
        if code[0].lower() == option:
            return option
    print("\nPlease try again")
    return get_option(my_codes, my_description)

my_codes = ['Q', 'B', 'S', 'P']
my_descriptions = ['Quit', 'Buy', 'Sell', 'Panic']
choices = get_option(my_codes, my_descriptions).lower()

while choices != 'q':
    if choices == 'q':
        break
    elif choices == 'b':
        print("Buy more and save even more!")
    elif choices == 's':
        print("Sell and earn big money now!")
    elif choices == 'p':
        print("The yen is down, oil is down, abandon all hope - PANIC")
    else:
        print("this is not an option")
    choices = get_option(my_codes, my_descriptions).lower()

print("Done")