#!/usr/bin/env python
#encoding:UTF-8

import random

#交叉
def cross_fun(self, s, alfa, s_cross, mul_cross):

    rand_table=range(0, len(s))         #生成种群的下标位表
    random.shuffle(rand_table)          #将下标位表随机化 

    """
    按照随机化的下标位表， 将种群两两交叉
    在DNA单条下标位中（不包括0位）随机选取一个或多个交叉位点
    """
    def iner_one():
	for i in xrange(0, int(len(s)*alfa)-1, 2):
	    t=random.choice(s_cross)
	    s[rand_table[i]], s[rand_table[i+1]]=(s[rand_table[i]]&t[0])+(s[rand_table[i+1]]&t[1]), (s[rand_table[i+1]]&t[0])+(s[rand_table[i]]&t[1])

    def iner_mul():
	for i in xrange(0, int(len(s)*alfa), 2):
	    for j in xrange(mul_cross[1]):
	        t=random.choice(s_cross)
	        s[rand_table[i]], s[rand_table[i+1]]=(s[rand_table[i]]&t[0])+(s[rand_table[i+1]]&t[1]), (s[rand_table[i+1]]&t[0])+(s[rand_table[i]]&t[1])


    def iner_mul_r():
	for i in xrange(0, int(len(s)*alfa), 2):
	    for j in xrange(random.randint(1, mul_cross[1])):
	        t=random.choice(s_cross)
	        s[rand_table[i]], s[rand_table[i+1]]=(s[rand_table[i]]&t[0])+(s[rand_table[i+1]]&t[1]), (s[rand_table[i+1]]&t[0])+(s[rand_table[i]]&t[1])


    if mul_cross[0]==False:
	iner_one()
    elif mul_cross[2]==False:
	iner_mul()
    else:
	iner_mul_r()

