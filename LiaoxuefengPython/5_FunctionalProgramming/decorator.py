# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print(fn) if fn.__str__()==fn else print('no metric args')
            start_time=time.time()
            return (func(*args,**kw),print('%s executed in %s ms' % (func.__name__, time.time()-start_time)))[0]
        return wrapper
    return decorator if fn.__str__()==fn else decorator(fn)

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric('test')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')
