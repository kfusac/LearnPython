# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

LL = list(filter(is_odd, range(1, 20)))

print(LL)

L=list(filter(lambda x:x%2==1,range(1,20)))

print(L)