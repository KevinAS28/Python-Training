#!/usr/bin/python

print 'penggunaan while if dan continue'
i = 0
while True:
  i = i + 1
  if i == 2:
   print 'lewatin 2'
   continue
  if i == 5:
   print 'break'
   break
  print i
  
print 'selsai'

print ' '

print 'lagi'
print ' '
apa = 2 
while True:
 apa = apa + 2     #KALI INI SPASI HARUS TEPAT
 if apa == 20:
  print 'lanjut'
  continue
 if apa == 40:
  print 'selsai'
  break 
 print apa   #LINE INI SPASI HARUS MUNDUR:PERHATIKAN

print ' '
print 'Penggunaan Lists'
print ' '
kata = ["I","DID","IT"]
print kata[1]
print kata[0]  #ga perlu penjelasan lah
print kata[2]
print ' '
print 'empty list'
#empty = ksong

