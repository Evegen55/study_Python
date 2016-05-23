'''
Created on 23.05.2016

@author: Evegen
'''
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
        




an = PartyAnimal()
an.party()