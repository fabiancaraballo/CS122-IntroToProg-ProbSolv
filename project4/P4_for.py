top_movies = ["Pulp Fiction", "Scarface", "Step Brothers", "The Godfather"]
movies_list = len(top_movies)
print("Good Movies")
print("")
for i in range(movies_list):
	print(top_movies[i])



numbers = [5, 9, 26, 4, 21, -6]
num = len(numbers)
for i in range(num):
	if(i % 2 == 0):
		numbers[i] = numbers[i]
	elif(i % 2 == 1):
		numbers[i] = numbers[i] * 2

print("Modified List")
print(numbers)
