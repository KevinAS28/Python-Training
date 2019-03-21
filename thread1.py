#!/usr/bin/python

from threading import Thread
import time

jawab = None

def inp():
 jawab = input('kata-kata : ')
 return jawab = jawab

def waktu(sec):
 time.sleep(sec)
 if jawab != None:
  return
 print("""
too slow baby""")
 exit()

oke = Thread(target=inp, args=[])
eko = Thread(target=waktu, args=[5])

oke.start()
eko.start()
