#!/usr/bin/python

import time
import random
import string

while True:

 lis = list(string.ascii_uppercase)
 ran = str(random.choice(lis))
 mac = (str('(') + ran + ran + str(':') + ran + ran + str(':') + ran + ran + str(')'))
 print('MONINTORING IP AND PORT(HONEYPOT ACTIVATED) %s' % (mac))
 time.sleep(1)  
