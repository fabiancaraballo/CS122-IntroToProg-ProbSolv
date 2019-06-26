name = ""
grade_A = 57
grade_B = 43
grade_C = 33
grade_D = 25
name_list = []
grade_list = []
while(name != 'Quit'):
	name = input("First name (or Quit to end): ")
	grade = int(input("Points on test:"))
	if(name != "Quit"):
		grade_list.append(grade)
	if(name != "Quit"):
		name_list.append(name)
for i in range(len(grade_list)):
	if(grade_list[i] >= grade_A):
		print(name_list[i], grade_list[i], "A")
	elif(grade_list[i] >= grade_B):
		print(name_list[i], grade_list[i], "B")
	elif(grade_list[i] >= grade_C):
		print(name_list[i], grade_list[i], "C")
	elif(grade_list[i] >= grade_D):
		print(name_list[i], grade_list[i], "D")
	else:
		print(name_list[i], grade_list[i], "F")

