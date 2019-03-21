#!/usr/bin/python

print 'penggunaan elif'

nomor = 3
if nomor == 5:
 print 'nomor 5'
elif nomor == 4:    #jadi if nomor 5 print anu...elif print apa elif print apa
 print 'kece'
elif nomor == 2:
 print 'salah'
elif nomor == 3:
 print "bener"
print ' '
print ' '
print 'penggunaan and atau boolean magic'
lagi = 1 == 1 and 2==2
lagi1 = 1==1 and 2==3
print lagi
print lagi1
print 'penggunaan boolean magic kurung'
if(1==1) and (2+4>5):
 print 'benerbngt'
else:                  #ga bisa pake elif
 print 'salahbngt'