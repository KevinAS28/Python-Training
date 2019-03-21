import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("wow")
alex = turtle.Turtle()

col = ["red", "yellow", "green", "purple", "blue"]
alex.penup()
size = 20
co = 0
alex.color("white")
alex.shape("turtle")
for i in range(30):
 alex.color(col[co])
 alex.stamp()
 size = size + 3
 alex.forward(size)
 alex.left(24)
 co = co + 1
 if co == 5:
  co = 0

"""
size1 = 20
ales = turtle.Turtle()
ales.penup()
ales.color("white")
ales.shape("turtle")
for a in range(30):
 ales.color(col[co])
 ales.stamp()
 size1 = size1 + 3
 ales.forward(size1)
 ales.right(24)
 co = co + 1
 if co == 5:
  co = 0

"""
turtle.mainloop()
