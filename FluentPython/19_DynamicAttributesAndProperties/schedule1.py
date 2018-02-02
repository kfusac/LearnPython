#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: kfusac
@license: kfusac Licence 
@contact: kfusac@163.com
@software: FluentPython
@IDE:PyCharm
@file: schedule1.py
@time: 18/1/31 17:41
"""

import warnings
import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    """
    schedule1.py: traversing OSCON schedule data
    # BEGIN SCHEDULE1_DEMO
    >>> import shelve
    >>> db = shelve.open(DB_NAME)
    >>> if CONFERENCE not in db:
    ...     load_db(db)
    ...
    >>> speaker = db['speaker.3471']
    >>> type(speaker)
    <class 'schedule1.Record'>
    >>> speaker.name, speaker.twitter
    ('Anna Martelli Ravenscroft', 'annaraven')
    >>> db.close()
    """
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)
