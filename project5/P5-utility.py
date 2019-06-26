import turtle as t 

def ask_for_int(hint):
	temp = input(hint)
	value = int(temp)
	return value
height_hint = "Enter number: "
height = ask_for_int(height_hint)
next_number = height + 1 
print("You entered", height, ", next number is", next_number)

print("")


def ask_for_float(hint):
	decimal = input(hint)
	value = float(decimal)
	return value
float_hint = "Enter a decimal number with 3 decimals:"
answer = ask_for_float(float_hint)

print("")

def ask_for_str(hint):
	word = input(hint)
	value = word
	return value
string_hint = "Type your first name:"
name = ask_for_str(string_hint)

print("")

def make_money(answer):
	decimal = float(answer) 
	value = round(decimal, 2)
	return value
sum = make_money(answer)
print(sum)



print("")

def jump(distance):
	t.penup()
	t.forward(distance)
	t.pendown()
jump(100)

def jump_to(x,y):
	t.penup()
	t.goto(x,y)
	t.pendown
jump_to(120,50)











