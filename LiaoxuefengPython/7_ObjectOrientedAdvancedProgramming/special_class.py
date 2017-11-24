#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Chain(object):
    # def __init__(self,path=''):
        # self._path=path    
    # def __getattr__(self,path):
        # if path=='users':
            # return lambda name:Chain('%s/%s/%s'%(self._path,path,name))
        # else:
            # return Chain('%s/%s'%(self._path,path))        
    # def users(self,path):
        # return lambda name:Chain('%s/%s/%s'%(self.path,path,name))
    # def __str__(self):
        # return self._path
    # __repr__=__str__
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        if path == 'users':
            return lambda attr : Chain('%s/%s/%s' % (self._path, path, attr))
        else:
            return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    
if __name__=='__main__':
    # print(Chain().status.users.timeline.list)
    print(Chain().users('Bob').speos)