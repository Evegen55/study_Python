'''
Created on 25 мая 2016 г.

@author: Lartsev
'''

class MyClassTwo(object):
    '''
    classdocs
    '''
    x = 0
    name = ''
    def __init__(self, param):
        '''
        Constructor
        '''
        self.name = param
        print('I am constructed as ', self.name)
        

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
        self.name = 'Tommy'
    
    def __del__(self):
        print('I am destructed as',self.name, self.x )
        

anb = MyClassTwo('Sally')
anb.party()
anb.party()
anb.party()
anb.party()

an = MyClassTwo('Jimmy')