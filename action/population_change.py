#!/usr/bin/env python
#encoding:UTF-8

import random

#变异
def change_fun(self, s, belta, bit_len, s_change):
    def in_action():
        i = random.randint(0, len(s)-1)
        j = random.choice(s_change)
	s[i]=s[i]^j

 
    for x in xrange(int( bit_len*len(s)*belta )):
	in_action()

	
   
