#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: sample7-17.py
@time: 18/1/19 15:07
"""

import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kws):
        t0 = time.perf_counter()
        result = func(*args, *kws)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kws:
            pairs = ['%s=%r' % (k, w) for k, w in kws.items()]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[{0:.10f}s] {1}({2}) -> {3} '.format(elapsed, name, arg_str, result))
        return result

    return clocked
