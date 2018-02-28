#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: bulkfood_v3.py
@time: 18/2/1 14:35
"""


class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    '''
    >>> nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    >>> nutmeg.weight, nutmeg.price
    (8, 13.95)
    >>> sorted(vars(nutmeg).items())
    [('description', 'Moluccan nutmeg'), ('price', 13.95), ('weight', 8)]
    >>> truffle = LineItem('White truffle', 100, 0)
    Traceback (most recent call last):
    ...
    ValueError: value must be > 0
    '''
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
