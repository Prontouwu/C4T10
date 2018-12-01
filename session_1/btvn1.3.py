import turtle
win = turtle.Screen()
turtle.shape("turtle")
turtle.color("black")

turtle.speed(0)

for i in range(15) :
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)

win.exitonclick()