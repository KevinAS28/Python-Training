#!/usr/bin/python

print 'penggunaan and or not'
#and or  not itu boolean magic

print "(and:)"

boandst = 1 == 1 and 2 == 2 #kalo dua2ny bener true
print boandst
boandnd = 1 == 1 and 2 == 3
print boandnd

print " "

print "pake or" #kalo salah satu dari mereka atau dua2ny bener true

boorst = 1 == 1 or 2 == 2
boornd = 1==1 or 2==3
boorrd = 1==2 or 3==4

print boorst
print boornd
print boorrd

print ' '

print 'pake not' #cuma satu argument
bonotst = 1 == 1 #sma kaya 1 != 1
bonotnd = 2 == 3 

print bonotst 
print bonotnd

print ' '

print 'boolean pke if'

mjk = 1+1
if not True:
 print '1'
elif not (1+1 == 3):
 print ("2")
else:
 print '3'