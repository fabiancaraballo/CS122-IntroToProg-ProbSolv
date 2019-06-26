name_list = []
name = ""
while name != 'Quit':
	name = input("Type 'Quit' or name to add such as Jan Smith: ")
	name_list.append(name)
name_list.sort()
for i in range(len(name_list)):
	print(name_list[i])
print("Name list has", len(name_list), "names.")
print("")
print("----------")
print("Finished")