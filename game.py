#!/usr/bin/python
import os
import sys
import random

#game = "y"
#while game.lower() == "y":
print("you are using python version "+sys.version) 
print("""





""")
print("""

select the game:

1.pattern game
2.pin game

insert the number and hit enter

""")

menug = input("your choice? ")
 #game pattern
def diff():
 print("""

select difficulty:

1.easy
2.normal
3.hard

type the number and hit enter

""")


diff()
dif1 = input("your choice? ")


 #pattern easy
if dif1 == 1:
 num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
 ans = [random.choice(num), random.choice(num), random.choice(num)]
 print(ans)
  