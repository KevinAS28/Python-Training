#!/usr/bin//python3

from threading import Thread as th
from time import sleep as sl
import os
import sys
import time
import platform
import getpass
from Crypto.Cipher import AES

jawab = None
def periksa():
 sl(2)
 if jawab != None:
  return
 print("""
too slow baby""")
 try:
  raise KeyboardInterrupt
 except KeyboardInterrupt:

  exit()


trit = th(target = periksa, args = [])
trit.start()
jawab = input('message: ')

#periksa configuration file
cwd = os.getcwd()
print('now in dir %s' % (cwd))
sl(1)
print("""
now checking conf file at root dir
""")
"""
lanj = 0
null = 0
agg0 = 'Kevin'
agg1 = 'kEvin'
agg2 = 'keVin'
agg3 = 'kevIn'
agg4 = 'keviN'
for aaa in range(10):
 if null == 0:
  print(agg0, end='\r')
 elif null == 1:
  print(agg1, end='\r')
 elif null == 2:
  print(agg2, end='\r')
 elif null == 3:
  print(agg3, end='\r')
 elif null == 4:
  print(agg4, end='\r')
 else:
  print('error')
 null += 1
 if null == 4:
  lanj = 1
  null = 0
 sl(1)

"""
def spab(jml):
 for abc in range(jml):
  print(' ')
os.chdir('/')
os.access('rootkit.conf', os.W_OK)
with open('rootkit.conf', 'r') as file:
 print(file.read())
time.sleep(2)
spab(5)

with open('rootkit.conf', 'r') as filee:
 print(list(filee.readlines(1)))
 print(filee[0])


#okea = open('rootkit.conf', 'r')
#print(list(okea.readline(1))) 
