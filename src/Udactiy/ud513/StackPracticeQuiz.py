"""
Created on Nov 9, 2016
Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head
        if current:
            self.head = new_element
            new_element.next = current
        else:
            self.head = new_element  
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head
        if current:
            self.head = None
            self.head = current.next
            return current        

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)        

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()        
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value


"""
By Zaal: Write a program that reads in a sequence of characters and prints them in reverse order. Use a stack.
"""
class ReadStringReverse(object):
    def __init__(self,word=None):
        self.word = word        
    
    def read_reverse(self):
        i = 0
        k = 0
        wrd = self.word
        stack = Stack(Element(wrd[i]))        
        while i < len(wrd):
            stack.push(Element(wrd[i]))
            i = i + 1
        while k < len(wrd):
            print stack.pop().value
            k = k + 1

w1 = "REVERSE"
       
rev = ReadStringReverse(w1)
rev.read_reverse()            
        
