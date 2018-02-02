#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: sample7-25.py
@time: 18/1/19 16:56
"""

import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*_args, **kws):
            t0 = time.perf_counter()
            result = repr(func(*_args, **kws))
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = []
            if _args:
                arg_lst.append(', '.join(repr(arg) for arg in _args))
            if kws:
                pairs = ['%s=%r' % (k, w) for k, w in kws.items()]
                arg_lst.append(', '.join(pairs))
            args = ', '.join(arg_lst)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorate


if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)
