# -*- coding: utf-8 -*-
import re

def name_of_email(addr):
    # re_email=re.compile(r'^(\<(?P<name>.+)\>(.+?)|(?P<name1>\w[\w.]+)@(\w+)\.(\w{2,4})')
    re_email=re.compile(r'(<(?P<name>.+?)>)?\s*(?P<name1>[a-zA-Z]+)@[a-zA-Z]+[.][a-zA-Z]{3}')
    m=re_email.match(addr)
    if m.group('name'):
        return m.group('name')
    elif m.group('name1'):
        return m.group('name1')
    else:
        return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')