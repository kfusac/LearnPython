#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: osconfeed.py
@time: 18/1/31 14:37
"""
import warnings
import os
import json

import requests

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    '''
    >>> feed = load()
    >>> sorted(feed['Schedule'].keys())
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed['Schedule'].items()):
    ...     print('{:3} {}'.format(len(value), key))
    ...
      1 conferences
    494 events
    357 speakers
     53 venues
    >>> feed['Schedule']['speakers'][-1]['name']
    'Carina C. Zona'
    >>> feed['Schedule']['speakers'][-1]['serial']
    141590
    >>> feed['Schedule']['events'][40]['name']
    'There *Will* Be Bugs'
    >>> feed['Schedule']['events'][40]['speakers']
    [3471, 5199]
    '''
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        r = requests.get(URL, stream=True)
        with open(JSON, 'wb') as local:
            local.write(r.text)

    with open(JSON, encoding='utf-8') as fp:
        return json.load(fp)
