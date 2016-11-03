'''
Created on Nov 3, 2016

@author: Evgenii_Lartcev
'''
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    
    score = 0
    
    def __init__(self):
        self.items = []
        self.score = 0;
        
    def addItem(self, word):
        self.items.append(word)
        if word == "tophat": self.score += 2
        elif word == "bowtie": self.score += 4
        elif word == "monocle": self.score += 5
    
    def getClassiness(self):
        return self.score

# Test cases
me = Classy()

# Should be 0
print me.getClassiness()

me.addItem("tophat")
# Should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print me.getClassiness()

me.addItem("bowtie")
# Should be 15
print me.getClassiness()