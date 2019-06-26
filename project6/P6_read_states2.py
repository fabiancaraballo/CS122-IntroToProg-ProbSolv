lines_read = [ ]
with open('state_data.txt') as fileread:
    lines = fileread.read().splitlines()
	
for line in lines:
		line = line.strip("/n")
		state_line = line.split(",")
		lines_read.append(state_line)
		#print(state_line)


def print_start(state_string):
    for state_info in lines_read:
        state_name = state_info[0].lstrip()
        #print(state_name.lstrip())
        if state_name.startswith(state_string):
            print(state_info)


def print_end(state_string):
    for state_info in lines_read:
        state_name = state_info[0].lstrip()
        #print(state_name.lstrip())
        if state_name.endswith(state_string):
            print(state_info)


def print_contains(state_string):
    for state_info in lines_read:
        state_name = state_info[0].lstrip()
        #print(state_name.lstrip())
        if state_string in state_name:
            print(state_info) 



print("Options: ")
print("S Starts with")
print("C Contains")
print("E Ends with")
print("Q Quit")


word = input("Type the option you want: ")
word = word.lower()
while word != 'QUIT':
    lines_read.append(word)
    if word == "s":
        word2 = input("What letters does state name start with: ")
        print_start(word2)
        word = input("Type the option you want: ")

    elif word == "c":
        word2 = input("What letters does state name contain: ")
        print_contains(word2)
        word = input("Type the option you want: ")

    elif word == "e":
        word2 = input("What letters does state name end with: ")
        print_end(word2)
        word = input("Type the option you want: ")



    




