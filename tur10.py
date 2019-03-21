#!/usr/bin/python

import turtle
from turtle import *

agusto = turtle.Screen()
kevin = turtle.Turtle() # lingkaran besar
kevinn = turtle.Turtle() #lingkaran kecil
kevinnn = turtle.Turtle() #spiral

kevin.hideturtle()
kevinn.hideturtle()
#kevinnn.hideturtle()

agusto.bgcolor("black")
agusto.title("mantap jiwa")


kevinn.color("lightgreen")
kevinn.speed(0)
kevinn.right(90)
kevinn.forward(50)
kevinn.left(90)


#spiral
def spiral(loo):

 kevinnn.penup()
 kevinnn.color("lightgreen")
 kevinnn.speed(0)
 kevinnn.forward(60)
 kevinnn.left(90)
 kevinnn.pendown()
 kevinnn.forward(275)
 for b in range(180):
  kevinnn.left(1)
  kevinnn.forward(1)
 kevinnn.forward(550)
 for c in range(180):
  kevinnn.left(1)
  kevinnn.forward(1)
 kevinnn.forward(275)

def spirall(lo):

 kevinnn.forward(275)
 for b in range(180):
  kevinnn.left(1)
  kevinnn.forward(1)
 kevinnn.forward(550)
 for c in range(180):
  kevinnn.left(1)
  kevinnn.forward(1)
 kevinnn.forward(275)


spiral(1)

for f in range(360):
 angk = 1
 kevinnn.right(angk)
 spirall(1)
 angk += 1
#spiral(1)

#lingkaran kecil kevinn
for a in range(360):
 kevinn.left(1)
 kevinn.forward(1)



kevin.penup()
kevin.color("lightgreen")
kevin.speed(10)
kevin.right(90)
kevin.forward(300)
kevin.left(90)
kevin.pendown()

#lingkaran besar kevin
for x in range(360):
 kevin.left(1)
 kevin.forward(5)


turtle.mainloop()
