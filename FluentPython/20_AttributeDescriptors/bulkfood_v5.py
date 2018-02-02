#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: bulkfood_v5.py
@time: 18/2/1 15:29
"""
import model_v5 as model


class LineItem:
    '''
    >>> nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    >>> nutmeg.weight, nutmeg.price
    (8, 13.95)
    >>> truffle = LineItem('White truffle', 100, 0)
    Traceback (most recent call last):
    ...
    ValueError: value must be > 0
    '''
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
