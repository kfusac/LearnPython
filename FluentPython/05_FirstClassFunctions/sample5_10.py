#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: sample5_10.py
@time: 18/1/5 15:50
"""


def create_tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join('{0}="{1}" '.format(attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<{0} {1}>{2}</{0}>'.format(name, attr_str, c)
                         for c in content)
    else:
        return '<{0} {1} />'.format(name, attr_str)
