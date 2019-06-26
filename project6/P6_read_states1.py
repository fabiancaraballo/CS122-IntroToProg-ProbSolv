lines_read = [ ]
with open('state_data.txt') as fileread:
    lines = fileread.read().splitlines()
	
for line in lines:
		line = line.strip("/n")
		state_line = line.split(",")
		lines_read.append(state_line)
		#print(state_line)


def print_states(state_string):
    for state_info in lines_read:
        state_name = state_info[0].lstrip()
        #print(state_name.lstrip())
        if state_name.startswith(state_string):
            print(state_info)


word = input("Type a state or start of state name or QUIT to end: ")
print_states(word)
while word != 'QUIT':
    lines_read.append(word)
    word = input("Type a state or start of state name or QUIT to end: ")
    print_states(word)
            






    
