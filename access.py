#!/usr/bin/python3

import os

os.chdir('aes')
chk = os.access("korban1.txt", os.W_OK)
print(chk)