#!/usr/bin/python

import turtle
from turtle import *

agusto = turtle.Screen()
kevin = turtle.Turtle()

agusto.title("kevin")
agusto.bgcolor("black")

leftt = 5
size = 3
co = 0
col = ["red", "yellow", "green", "purple", "blue", "pink"]

for i in range(100):
	kevin.color(col[co])
	kevin.pensize(size)
	kevin.hideturtle()
	kevin.left(10)
	kevin.forward(leftt)
	co += 1
	size += 1
	if co == 6:
		co = 0
	leftt += 1
leftt = 5
size = 3
kevinn = turtle.Turtle()
for i in range(100):
	kevinn.color(col[co])
	kevinn.pensize(size)
	kevinn.hideturtle()
	kevinn.right(10)
	kevinn.forward(leftt)
	co += 1
	size += 1
	if co == 6:
		co = 0
	leftt += 1


turtle.mainloop()
