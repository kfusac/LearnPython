#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: sentence.py
@time: 18/1/25 15:01
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    '''
    Tests of sentence is iterable::
    >>> s = Sentence('"The time has come," the Walrus said,')
    >>> s
    Sentence('"The time ha... Walrus said,')
    >>> for word in s:
    ...     print(word)
    The
    time
    has
    come
    the
    Walrus
    said
    '''
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
