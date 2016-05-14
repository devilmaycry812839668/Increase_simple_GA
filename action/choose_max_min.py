#!/usr/bin/env python
#encoding:UTF-8
import random

#选择
def choose_fun(self, s, object_fun, s_choose, wheel):

    if wheel==False:
        #将最小的个体替换为最大的个体       
        s_max=max(s, key=lambda x:object_fun([(t[0]&x)/t[1] for t in s_choose]))#找出最大的个体
        s_min=min(s, key=lambda x:object_fun([(t[0]&x)/t[1] for t in s_choose]))#找出最小的个体

        loc_max=s.index(s_max)              #找出最大的个体位置
        loc_min=s.index(s_min)              #找出最小的个体位置
        s[loc_min]=s_max 
    else:
	f=lambda x:object_fun([(t[0]&x)/t[1] for t in s_choose])
        temp0=[f(x) for x in s]
	wheel_sum=sum(temp0)
        temp0[0]=temp0[0]/(1.0*wheel_sum)

	for i in xrange(1, len(temp0)-1):
	    temp0[i]=temp0[i-1]+temp0[i]/(1.0*wheel_sum)

        temp0[len(temp0)-1]=1.0
        
        s_temp=[]
	for i in xrange(len(temp0)):
	    r=random.random()        
	    for j in xrange(len(temp0)):
		if r<=temp0[j]:
		    s_temp.append(s[j])
		    break

	s[:]=s_temp
	
	



