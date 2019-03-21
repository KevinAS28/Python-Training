#!/usr/bin/python

print 'masih list yang beroperasi...jadi LETS GO'
kata = ["nothing","to","see","here"]
print "to" in kata
print "nothing" in kata
print "aku" in kata

print ' '
print 'lisst emang simple..pake if dan in'
nomor = [10,9,8,7,6,5]
nomor[0] = nomor[1] - 5
if 4 in nomor:
 print nomor[3]
else:
 print nomor[4]

print ' '
print 'list pake not dan in'
apaan = [1,2,3]
print not 4 in apaan #tdk ada 4 in apaan....true
print 4 not in apaan
print not 3 in apaan #tdk ada 3 in apaan....salahFALSE
print 3 not in apaan

print ' '
print 'list function....asekk...kece'
aseek = [1,2,3]
aseek.append(4) #pake append menambahkan item di akhir list yang sdh ad
print aseek

print ' '
print 'function len'
asoy = [3,5,1,5,6,1]
print len(asoy) #len untuk gitu lah...itu di list ada 6 item jd 6 #hasilnya

print ' '
print 'fucntion insert pada list'
joz = ["python","fun"]
index = 1         #bisa juga g pke index joz.insert(2,"kawan")
joz.insert(index,"is")                        #2 diatas itu posisi
print joz

print ' '
print ''
