#!/usr/bin/python
import turtle
from turtle import *
import random

agusto = turtle.Screen()
kevin = turtle.Turtle()
kevin1 = turtle.Turtle()
agusto.bgcolor('black')
agusto.title('mantap jiwa')
col = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']
colll = 0
si = 50
kevin.color('white')
kevin.speed(10)

def minisr(x):
 for i in range(5):
  kevin.color(col[x])
  kevin.forward(50)
  kevin.right(90)
 

def squarer(coll):
 kevin.penup()
 kevin.left(90)
 plur = kevin.forward(50)
 kevin.forward(300)
 kevin.right(90)
 kevin.forward(650)


 coll = 0

 kevin.right(90)
 kevin.pendown()
 for a in range(14):
  minisr(coll)
  coll += 1
  tuf = kevin.left(90)
  if coll == 6:
   coll = 0
 

squarer(1)
"""
for i in range (10):
 squarer(1)
 si += 50
 coll += 1
 if coll == 6:
  coll = 1
"""
turtle.mainloop()
 
