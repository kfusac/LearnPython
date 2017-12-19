import itertools

'''
观察者模式实现
'''

class Publisher:

    def __init__(self):
        self.observers=set()

    def add(self,observer,*observers):
        for observer in itertools.chain((observer,),observers):
            self.observers.add(observer)
            observer.update(self)
        else:
            print('Failed to add: %s' % observer)

    def remove(self,observer):
        try:
            self.observers.discard(observer)
        except ValueError:
            print('Failed to remove: %s' % observer)

    def notify(self):
        [observer.update(self) for observer in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self,name):
        Publisher.__init__(self)
        self.name=name
        self._data=0

    def __str__(self):
        return  "%s: '%s' has data= %s"%(type(self).__name__,self.name,self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,new_value):
        try:
            self._data=int(new_value)
        except ValueError as e:
            print('Error: %s' % e)
        else:
            self.notify()

class HexFormatter:
    def update(self,pulisher):
        print("%s: '%s' has now hex data= %s"%(type(self).__name__,pulisher.name,hex(pulisher.data)))

class BinaryFormatter:
    def update(self,pulisher):
        print("%s: '%s' has now bin data= %s"%(type(self).__name__,pulisher.name,bin(pulisher.data)))

#测试
def main():
    df=DefaultFormatter('test1')
    print(df)
    
    print()
    hf=HexFormatter()
    df.add(hf)
    df.data=3
    print(df)
    
    print()
    bf=BinaryFormatter()
    df.add(bf)
    df.data=40
    print(df)
    
    print()
    df.remove(hf)
    df.data=40
    print(df)
    
    print()
    df.remove(hf)
    df.add(bf)
    
    df.data='hello'
    print(df)
    
    print()
    df.data=4.2
    print(df)

if __name__=='__main__':
    main()