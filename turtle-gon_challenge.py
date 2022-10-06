import turtle
sides = int(input("How many sides?"))
turtle.goto(0, 0)
turtle.pendown()
for x in range(sides):
    turtle.forward(100)
    turtle.left(360/sides)
turtle.exitonclick()
# LESS THAN 10 LINES LETS GO
