import turtle
win = turtle.Screen()
turtle.shape("turtle")
turtle.color("black")
# for i in range(4) : 
i = 1
while i < 5 : 
    turtle.forward(100)
    turtle.left(90)
    i = i + 1   
win.exitonclick()