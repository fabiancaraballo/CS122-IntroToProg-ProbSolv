import turtle as t 

t.pencolor("red")
t.pensize(2)
t.speed("fastest")
t.left(90)
size = 20
angle = 90
nudge = 4.7
bump = 5



for i in range(60):

	for i in range(4):
		t.forward(size)
		t.left(angle)


	t.right(nudge)
	t.forward(bump)
	size = size +4
	
