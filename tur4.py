import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("mantap")

alex = turtle.Turtle()
alex.color("white")
alex.pensize(3)

col = ["yellow", "white", "blue", "red", "green"]
for i in col:
 alex.color(i)
 alex.speed(1)
 alex.forward(50)
 alex.left(90)
 
 

turtle.mainloop()
 
