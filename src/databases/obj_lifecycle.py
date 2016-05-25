'''
Created on 25 мая 2016 г.

@author: Lartsev
'''

class MyClass(object):
    '''
    classdocs
    '''
    x = 0
    def __init__(self):
        '''
        Constructor
        '''
        print('I am constructed')
        

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
    
    def __del__(self):
        print('I am destructed', self.x)
        

an = MyClass()
an.party()
an.party()
an.party()
an.party()