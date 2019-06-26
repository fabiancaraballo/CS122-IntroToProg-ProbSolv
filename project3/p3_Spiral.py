import turtle as t 

t.pencolor("red")
t.pensize(2)
t.speed("fastest")
t.left(90)
size = 20
angle = 90
nudge = 4.7
bump = 5
color_list = ["red", "blue", "green", "yellow", "black", "white"]


for i in range(60):

	
	somecolor = color_list[i%len(color_list)]
	t.begin_fill()
	t.fillcolor(somecolor)
	for i in range(4):
		t.forward(size)
		t.left(angle)
	t.end_fill()
	t.right(nudge)
	t.forward(bump)
	size = size +4
	