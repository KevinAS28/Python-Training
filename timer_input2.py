from threading import Thread
import time
import sys

a = None

def get():
 global a
 a = input('press Y now! ')
 



def timer():
 time.sleep(2)
 if a != 'Y'.lower():
  print('\ntoo slow\n')
  sys.exit()

c = Thread(target = get, args = [])
d = Thread(target = timer, args = [])

d.start()
c.start()
