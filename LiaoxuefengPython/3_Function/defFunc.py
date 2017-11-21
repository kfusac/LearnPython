# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    for op in (a,b,c):
        if not isinstance(op,(int,float)):
            raise TypeError('bad operand type')
    if a==0:
        x1=-b/c
        x2=x1
    else:
        temp=b*b-4*a*c
        if temp>=0:
            x1=(-b+math.sqrt(temp))/(2*a)
            x2=(-b-math.sqrt(temp))/(2*a)
        else:
            x1=complex(-b/2*a,math.sqrt(-temp)/(2*a))
            x2=complex(-b/2*a,-math.sqrt(-temp)/(2*a))
    return x1,x2
    
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')