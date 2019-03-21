#!/usr/bin/python

#import module
import os 
import time
import random
import sys
from threading import Thread


if True:
 print ("written by kevin agusto "+(sys.version))
 print(" ")
 print("3.5.3 is recomended")
 time.sleep(2)

 
 a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 b = [(random.choice(a)), (random .choice(a)), (random.choice(a))]
 b.sort()
 rans0 = int(b[0])
 rans1 = int(b[1])
 rans2 = int(b[2])
 c = [" "]

 #supaya tidak ada yang sama
 if (rans0 == rans2) and (rans0 == rans1) and (rans2 == rans1):
  print("maaf ada kesalahan pada program.silahkan jalankan ulang programnya")
  time.sleep(3)
#  b = [(random.choice(a)), (random .choice(a)), (random.choice(a))]
#  b.sort()
#  rans0 = int(b[0])
#  rans1 = int(b[1])
#  rans2 = int(b[2])
#  c = [" "]
  print(rans0, rans1, rans2)
  exit()
  
 if rans0 == rans1:
  print("maaf ada kesalahan pada program.silahkan jalankan ulang programnya")
  time.sleep(3)
  print(rans0, rans1, rans2)
  exit()


 if rans2 == rans1:
  print("maaf ada kesalahan pada program.silahkan jalankan ulang programnya")
  time.sleep(3)
  print(rans0, rans1, rans2)
  exit()


 def hadiah1():
  print("""
  +-------------------------------------------------------+
  |               PIN GAME BY KEVIN AGUSTO                |
  +---------------------------+---------------------------+
  |      __________________   |  ___________              |
  |  ==c(______(o(______(_()  | |           |======[***   |
  |             )=\           | |  ANDA      \            |
  |            //  \          | |_____________\_______    |
  |           //    \         | |==[WOW >]============\   |
  |          //      \        | |______________________\  |
  |         //SELAMAT \       | \(@)(@)(@)(@)(@)(@)(@)/   |
  |        //          \      |  *********************    |
  +---------------------------+---------------------------+
  |      o O o                |        \'\/\/\/'/         |
  |              o O          |         )======(          |
  |                 o         |       .' MENANG '.        |
  | |^^^^^^^^^^^^^^|l___      |      /    _||__   \       |
  | |    TELAH       |""\___, |     /    (_||_     \      |
  | |________________|__|)__| |    |     __||_)     |     |
  | |(@)(@)"" **|(@)(@)**|(@) |    "       ||       "     |
  |  = = = = = = = = = = = =  |     '--------------'      |
  +---------------------------+---------------------------+


""")


 def ms():
  print("""





















""")
 def ms1():
  print("""







""")


 #perfect
 ms()
 time.sleep(2)
 print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
 print(" ")
 print(" ")
 print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
 print(" ")
 print(" ")
 print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
 ms1()

 def perfect():
  ms()
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()


 
#jika 1
 time.sleep(2)
 if (rans0 == a[0]) or (rans1 == a[0]) or (rans2 == a[0]):

  ms()
  
  print(c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()

#jika 2
 if (rans0 == a[1]) or (rans1 == a[1]) or (rans2 == a[1]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()

#jika 3
 if (rans0 == a[2]) or (rans1 == a[2]) or (rans2 == a[2]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], c[0])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()

#jika 4
 if (rans0 == a[3]) or (rans1 == a[3]) or (rans2 == a[3]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()


#jika 5
 if (rans0 == a[4]) or (rans1 == a[4]) or (rans2 == a[4]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()



#jika 6
 if (rans0 == a[5]) or (rans1 == a[5]) or (rans2 == a[5]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], c[0])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()


#jika 7
 if (rans0 == a[6]) or (rans1 == a[6]) or (rans2 == a[6]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[7], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()



#jika 8
 if (rans0 == a[7]) or (rans1 == a[7]) or (rans2 == a[7]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], c[0], c[0], c[0], c[0], a[8])
  ms1()
  time.sleep(2)
  perfect()

#jika 9
 if (rans0 == a[8]) or (rans1 == a[8]) or (rans2 == a[8]):

  ms()
  
  print(c[0], c[0], c[0], a[0], c[0], c[0], c[0], a[1], c[0], c[0], c[0], a[2])
  print(" ")
  print(" ")
  print(c[0], c[0], c[0], a[3], c[0], c[0], c[0], a[4], c[0], c[0], c[0], a[5])
  print(" ") 
  print(" ")
  print(c[0], c[0], c[0], a[6], c[0], c[0], c[0], a[7], c[0], c[0], c[0], c[0])
  ms1()
  time.sleep(2)
  perfect()


 b.sort()



 #masukan input
 print("""

angka berapa saja tadi yang hilang2an?
(harus berurutan)
hitugan 10 detik dari sekarang!

""")

#minta jawaban dan mengkoreksinya

# jawab0 = None
# jawab1 = None
# jawab2 = None 


# jawabrr = [jawabb0, jawabb1, jawabb2]
# jawabrr.sort
# jawabr0 = jawabrr[0]
# jawabr1 = jawabrr[1] 
# jawabr2 = jawabrr[2]


# if (jawabr[0] == rans0) and (jawabr[1] == rans[1]) and (jawab[2] == rans[2]):
#  print("anda menang!!! selamat yaaa!!! ;) ")
#  time.sleep(3)
#  print(rans0, rans1, rans2)
#  exit()
# else:
#  print("anda kalah.silahkan coba lagi")
#  exit()



 def periksa():
  try:
   time.sleep(5)
#  print(jawabr0, jawabr1, jawabr2)
 
   if ((jawabr0) == (rans0)) and ((jawabr1) == (rans1)) and ((jawabr2) == (rans2)):
#    print("menang")
    hadiah1()
    print(rans0, rans1, rans2)
    print(jawabr0, jawabr1, jawabr2)
    exit()
    return  
   print("""
 kalah""")
   exit()
  except NameError:
   ms()
   print("waktu habis")
   exit()

#   ms()
#   print("waktu habis.anda kalah")
   
# print(rans0 == jawabr0)

 Thread(target = periksa).start()

 

 try:
  jawab0 = input("jawaban mu? ")
  jawab1 = input("jawaban mu? ")
  jawab2 = input("jawaban mu? ") 

  jawabrr = [jawab0, jawab1, jawab2]
  jawabrr.sort()
  jawabr0 = int(jawabrr[0])
  jawabr1 = int(jawabrr[1])
  jawabr2 = int(jawabrr[2])
  print(rans0, rans1, rans2)
  print(jawabr0, jawabr1, jawabr2)
 except:
  exit()



 print(rans0, rans1, rans2)
 print(jawabr0, jawabr1, jawabr2)
