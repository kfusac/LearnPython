# -*- coding: utf-8 -*-

def normalize(name):
    return name[0].upper()+name[1:].lower()
    pass

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(lambda x,y:x*10+y,map(char2num,s[:s.index('.')]))+reduce(lambda x,y:x/10+y,map(char2num,s[-s.index('.'):][::-1]))/10

    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
