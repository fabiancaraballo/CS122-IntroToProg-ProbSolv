n = int(input("Enter a number from 10-20:"))
x = 7
print("Repeat", n , "times")
print("Powers of 7")
print("")

for i in range(n):
    print(x, "**", i, "is", x**i)