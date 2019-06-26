import random

roll_list = []
roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)
rolls = 1

while(roll_1 != 6 or roll_2 != 6):
	roll_list.append(roll_1)
	roll_list.append(roll_2)
	roll_1 = random.randint(1, 6)
	roll_2 = random.randint(1, 6)
	rolls += 1

roll_list.append(roll_1)
roll_list.append(roll_2)
print("Rolled", rolls, "dice as", rolls//2, "pairs of dice.")
print(roll_list)



	

