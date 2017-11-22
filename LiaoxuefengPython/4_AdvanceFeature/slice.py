# -*- coding: utf-8 -*-
def trim(str):
    if(len(str))==0 or (str[0]!=' ' and str[-1]!=' '):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    elif str[-1]==' ':
        return trim(str[:-1])
    

    
    
    
# 测试:
if trim('hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('') != '':
    print('4测试失败!')
elif trim('    ') != '':
    print('5测试失败!')
else:
    print('测试成功!')