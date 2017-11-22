# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if not isinstance(L,(list,tuple)):
        raise TypeError('L is not list or tuple')
    if len(L)==0:
        return (None, None)
    min=max=L[0]
    for n in L:
        if min>n: min=n
        if max<n: max=n
    return min,max

    
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')