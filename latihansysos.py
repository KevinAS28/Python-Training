#!/usr/bin/python

#latihan os dan sys

import os
import sys

def spab(x):
 for cbc in range(x):
  print(' ')

lines = [line.rstrip('\n') for line in (os.popen('ls'))]
print(lines)
spab(5)

