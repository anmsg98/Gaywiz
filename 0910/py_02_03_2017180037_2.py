import turtle
turtle.speed(8)
turtle.penup()
turtle.goto(-400,300)
turtle.pendown()
for i in range(6):
	turtle.forward(500)
	turtle.penup()
	turtle.backward(500)
	turtle.right(90)
	turtle.forward(100)
	turtle.left(90)
	turtle.pendown()
turtle.penup()
turtle.goto(-400,300)
turtle.right(90)
turtle.pendown()
for i in range(6):
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
turtle.exitonclick()
