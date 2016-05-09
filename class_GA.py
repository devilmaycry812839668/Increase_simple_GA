#!/usr/bin/python
#encoding:UTF-8
import random
import time
import action.population_init as p_init
import action.choose_max_min as c_max_min
import action.population_cross as p_cross
import action.population_change as p_change

random.seed(time.time())

#not bug 函数全部self, 若没有多线程也不会冲突,动态语言特性
class Genetic(object):
    """
    class_GA 是标准遗传算法的类形式
    increase版本比Simple_G_A版本提示在25%到28%之间。

    输入参数：
    bit_len, p_n, alfa, belta, object_fun, N, x_tuple, mul_cross

    s=[] 存放种群的列表
    s_choose=[] 选择操作的辅助二进制位列表
    s_cross=[] 交叉操作的辅助二进制位列表
    s_change=[] 变异操作的辅助二进制位列表
    bit_len 个体二进制位长度
    p_n 种群个体数
    alfa 交叉率
    belta 变异率
    object_fun 目标函数
    N 迭代次数
    x_tuple 变量x1, x2, x3等，二进制位长度, 为元组

    多点交叉参数:是否多点交叉， 交叉点数目是否随机，基准交叉点数
    mul_cross=(False, None, False)
    如果不开启多点交叉即第一个元素为False，元组的后两个元素可以输入任意值
    """

    class paramError(Exception):
        pass
    def param_check(self):
	if type(bit_len)!=int:
	    raise self.paramError, "param bit_len is wrong, it must be int"
        if type(p_n)!=int and type(p_n)!=long:
	    raise self.paramError, "param p_n is wrong, it must be int or long"
        if not (bit_len>1 and p_n>1):
	    raise self.paramError, "scope of bit or p_n is wrong"
        if type(alfa)!=float:
	    raise self.paramError, "param alfa is wrong, it must be float"
	if type(belta)!=float:
	    raise self.paramError, "param belta is wrong, it must be float"
        if not 0<alfa<1:
	    raise self.paramError, "scope of param alfa is wrong"
	if not 0<belta<1:
	    raise self.paramError, "scope of param belta is wrong"
	if type(N)!=int and type(N)!=long:
	    raise self.paramError, "param N  is wrong, it must be int or long"
        if type(x_tuple)!=tuple:
	    raise self.paramError, "param x_tuple is wrong, it must be tuple"
        for i in x_tuple:
	    if type(i)!=int:
	        raise self.paramError, "each of x_tuple  must be int"
            if not (1<=i<=bit_len):
		raise self.paramError, "scope of each of x_tuple wrong" 
    	if sum(x_tuple)!=bit_len:
            raise self.paramError, "param sum(x_tuple) must equal bit_len"
        if type(mul_cross)!=tuple or len(mul_cross)!=3:
	    raise self.paramError, "mul_cross must be tuple and have 3 elements"
	if mul_cross[0]!=False:
	    if mul_cross[0]!=True:
		raise self.paramError, "param mul_cross[0] must be bool"
	    elif type(mul_cross[1])!=int:
		raise self.paramError, "param mul_cross[1] must be int"
	    elif not (1<mul_cross[1]<bit_len):
		raise self.paramError, "scop of mul_cross[1] is wrong"
	    elif type(mul_cross[2])!=bool:	
		raise self.paramError, "mul_cross[2] must be bool"

	try:
	    object_fun((0, )*len(x_tuple))
	    object_fun( tuple(2**i-1 for i in x_tuple)  )
	except Exception, e:
	    print "function object maybe wrong"
	    raise self.paramError, e


    def __init__(self, bit_len, p_n, alfa, belta, object_fun, N, x_tuple, mul_cross=(False, None, False)):
	self.param_check()
        #初始化
	self.s=[]#存放种群的列表
	self.s_choose=[]#选择操作的辅助二进制位列表
	self.s_cross=[]#交叉操作的辅助二进制位列表
	self.s_change=[]#变异操作的辅助二进制位列表
        self.bit_len=bit_len#个体二进制位长度
	self.p_n=p_n#种群个体数
	self.alfa=alfa#交叉率
	self.belta=belta#变异率
	self.object_fun=object_fun#目标函数
	self.N=N#迭代次数
	self.x_tuple=x_tuple#变量x1, x2, x3等，二进制位长度
        """
	多点交叉参数:是否多点交叉， 交叉点数目是否随机，基准交叉点数
        """
        self.mul_cross=mul_cross


        self.p_start_fun=p_init.p_start_fun
	self.l_start_fun=p_init.l_start_fun
	self.choose_start_fun=p_init.choose_start_fun

        self.p_start_fun(self, self.bit_len, self.p_n, self.s)
	self.l_start_fun(self, self.bit_len, self.s_cross, self.s_change)
	self.choose_start_fun(self, self.s_choose, self.x_tuple, self.bit_len)

	"""
	或者写为如下 		       
        Genetic.p_start_fun=p_init.p_start_fun
	Genetic.l_start_fun=p_init.l_start_fun
	Genetic.choose_start_fun=p_init.choose_start_fun

        self.p_start_fun(self.bit_len, self.p_n, self.s)
	self.l_start_fun(self.bit_len, self.s_cross, self.s_change)
	self.choose_start_fun(self.s_choose, self.x_tuple, self.bit_len)
	"""
        self.choose_fun=c_max_min.choose_fun#选择
	self.cross_fun=p_cross.cross_fun#交叉
	self.change_fun=p_change.change_fun#变异


    def run(self):
        for i in xrange(N):# N 100000 :  迭代的次数
    	    self.choose_fun(self, self.s, self.object_fun, self.s_choose)#选择
            self.cross_fun(self, self.s, self.alfa, self.s_cross, self.mul_cross)    #交叉
            self.change_fun(self, self.s, self.belta, self.bit_len, self.s_change)#变异
    
    #目标函数的最大值
    def object_max_value(self):	    
	max_var=max(self.s, key=lambda x:object_fun([(t[0]&x)/t[1] for t in a.s_choose]))
	return object_fun([(t[0]&max_var)/t[1] for t in self.s_choose]) 
	

        
"""
#单元测试代码

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
"""

