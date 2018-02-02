#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: coroutil.py
@time: 18/1/26 15:19
"""

from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kws):
        gen = func(*args, **kws)
        next(gen)
        return gen

    return primer
