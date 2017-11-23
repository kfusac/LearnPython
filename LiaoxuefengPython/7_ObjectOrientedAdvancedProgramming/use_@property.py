# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        self.__width=value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        self.__height=value
        
    @property
    def resolution(self):
        return 786432
    pass

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')