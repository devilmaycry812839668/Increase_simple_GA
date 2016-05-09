#!/usr/bin/env python
#encoding:UTF-8

import random

#种群初始化
#l_sep 种群个体长度   l_len 种群个数
def p_start_fun(self, l_sep, l_len, s):    
    #二进制位数           DNA条数
    for i in xrange(l_len):
        s.append(random.randint(0, 2**l_sep-1))
 

#交叉操作的辅助二进制位列表
#变异操作的辅助二进制位列表
def l_start_fun(self, l_sep, s_cross, s_change):
    for i in xrange(l_sep):
        s_change.append(2**i)
    
    t=0
    for i in s_change[:-1]:
	t=t+i
	s_cross.append((2**l_sep-1-t, t))


#选择操作的辅助二进制位列表
def choose_start_fun(self, s_choose, s_tuple, l_sep):
   
    t=0
    for i in s_tuple:
        t=t+i
	s_choose.append( ( (2**i-1)*( 2**(l_sep-t) ), 2**(l_sep-t)) )




