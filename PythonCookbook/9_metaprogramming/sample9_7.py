#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: PythonCookbook
@IDE:PyCharm
@file: sample9_7.py
@time: 18/2/27 10:00
"""
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    '''
    >>> @typeassert(int, int)
    ... def add(x, y):
    ...     return x + y
    ...
    >>> add(2, 3)
    5
    >>> add(2,'hello')
    Traceback (most recent call last):
    ...
    TypeError: Argument y must be <class 'int'>
    >>> @typeassert(int, z=int)
    ... def spam(x, y, z=42):
    ...     print(x, y, z)
    ...
    >>> spam(1, 2, 3)
    1 2 3
    >>> spam(1, 'hello', 3)
    1 hello 3
    >>> spam(1, 'hello', 'world')
    Traceback (most recent call last):
    ...
    TypeError: Argument z must be <class 'int'>
    '''

    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorate
