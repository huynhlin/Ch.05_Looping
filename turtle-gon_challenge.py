import turtle
sides = int(input("How many sides?"))
turtle.penup
turtle.goto(0,0)
turtle.pendown()
angle = 360/sides
for x in range(sides):
    turtle.forward(100)
    turtle.left(angle)
