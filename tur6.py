import turtle
import time
from turtle import *

kevin = turtle.Screen()
agusto = turtle.Turtle()

kevin.bgpic("loading.gif")
kevin.title("hahahaha")


col = ["red", "yellow", "green", "purple", "blue"]
agusto.pensize(3)

ss = 0

for i in range(3):
 agusto.color(col[ss])
 agusto.forward(200)
 agusto.left(120)
 ss = ss + 1
 if ss == 6:
  ss = 0


time.sleep(5)

wow = turtle.Screen()
oww = turtle.Turtle()
wow.bgcolor("black")
wow.title("ahhh")

oww.pensize(3)
sss = 0

for o in range(4):
 oww.color(col[sss])
 oww.forward(100)
 oww.left(90)
 sss = sss + 1
 if sss == 6:
  sss = 0
turtle.mainloop()

