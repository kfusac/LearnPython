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
    >>> print('Back to normal.')
    Back to normal.
    >>> with looking_glass() as what:
    ...     a = 1/0
    Please DO NOT divide by zero!
    '''
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
