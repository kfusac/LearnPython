# -*- coding: utf-8 -*-
import re

def is_valid_email(addr):
    re_email=re.compile(r'^(\w[\w.]+)@(\w+)\.(\w{2,4})')
    if  re_email.match(addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')