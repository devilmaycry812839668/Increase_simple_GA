#!/usr/bin/env python
#encoding:UTF-8
from class_GA import *

#目标函数
#p 为每个DNA个体的二进制表示， 即 "11010101"
def object_fun(p):
    import math
    x=p[0]*10.0/(2**17-1)-5

    y=p[1]*10.0/(2**17-1)-5

    object_value =0.5-((math.sin( math.sqrt(x**2+y**2) ))**2-0.5)/(1+0.001*(x**2+y**2))**2

    return object_value

N=300#迭代的次数
alfa=0.6#交叉率
belta=0.01#变异率
p_n=200#DNA 条数
bit_len=34#每条DNA 二进制位长度
x_tuple=(17, 17)#(2, 4, 2) 变量x1, x2, x3等，二进制位长度
mul_cross=(False, None, False)#是否多点交叉， 交叉点数目是否随机，基准交叉点数
#mul_cross=(True, 3, True)

lll=[]
for i in xrange(1000):
    #a为生成的实例
    a=Genetic(bit_len, p_n, alfa, belta, object_fun, N, x_tuple, mul_cross)

    a.run()

    lll.append(a.object_max_value())
print sum(lll)/1000

