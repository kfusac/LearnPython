#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: mirror_gen.py
@time: 18/1/26 14:25
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    '''
    >>> with looking_glass() as what:
    ...     print('Alice, Kitty and Showdrop')
    ...     print(what)
    ...
    pordwohS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    '''
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
