# -*- coding: utf-8 -*-

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)

if __name__=='__main__':
    print(s)