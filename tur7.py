#!/usr/bin/python

import turtle
from turtle import *
import random
import time
wn = turtle.Screen()
#wn.bgpic("giphy.gif")
wn.title("tesss")
wn.bgcolor("black")

kevin = turtle.Turtle()
col = ["red", "yellow", "green", "purple", "blue", "pink"]
oke = 0#str(random.choice(col))

kevin.shape("turtle")
kevin.color(random.choice(col))
kevin.penup()
kevin.stamp()
kevin.right(90)
kevin.forward(200)
kevin.left(90)
kevin.forward(90)
kevin.left(30)
kevin.forward(150)
time.sleep(2)
for i in range(12):
 kevin.penup()
 kevin.color(col[oke])
 kevin.left(30)
 kevin.forward(150)
 kevin.stamp()
 oke += 1
 if oke == 6:
  oke = 0
 
 



"""
kevin.penup()
for a in range(2):
 kevin.left(90)
 kevin.forward(250)
for i in range(11):
 kevin.pendown()
 kevin.color(col[oke])
 kevin.stamp()
 kevin.left(30)
 kevin.penup()
 kevin.forward(150)
 oke += 1
 if oke == 6:
  oke = 0

"""






"""
if True:#for i in range(6):
 kevin.color(col[oke])
 kevin.forward(200)
 kevin.right(135)
 kevin.forward(300)
 kevin.right(150)
 kevin.forward(400)
 kevin.right(150)
 kevin.forward(400)
 kevin.right(150)
 kevin.forward(300)
 kevin.right(135)
 kevin.forward(200)
 
 

 oke += 1
 if oke == 6:
  oke = 0
"""
turtle.mainloop()

