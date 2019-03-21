#!/usr/bin/python

import socket
import string

mldi = 0
dicti = {}
dictii = {}
kata = list(string.ascii_lowercase)


for lala in range(26):
 dicti[kata[mldi]] = mldi
 dictii[mldi] = [kata[mldi]]
 mldi += 1
spasi = " "
kata.append(spasi)
dicti[spasi] = '/'

print(dicti)
print("============")
print(dicti['a'])
