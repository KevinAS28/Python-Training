#!/usr/bin/python
import time
from threading import Thread

answer = None

def check():
 time.sleep(10)
 if answer != None:
  return 
 print("oke")

Thread(target = check).start()
answer = input("aku ")
