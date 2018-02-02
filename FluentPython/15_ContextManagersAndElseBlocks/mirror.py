#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: mirror.py
@time: 18/1/26 14:13
"""


class LookingGlass:
    '''
    >>> with LookingGlass() as what:
    ...     print('Alice, kitty and snowdrop')
    ...     print(what)
    pordwons dna yttik ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'
    >>> print('Back to normal.')
    Back to normal.
    >>> with LookingGlass() as what:
    ...     a=1/0
    Please DO NOT divide by zero!
    '''

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
