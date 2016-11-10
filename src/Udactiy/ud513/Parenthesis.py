'''
@author: Evegen
'''
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
    
    def isEmpty(self):
        if self.ll.head == None: return True
        else: return False   

class CheckParenthesis(object):
    def __init__(self,word=None):
        self.word = word
        
    def check(self):
        stack = Stack(Element(None))
        for c in self.word:
            if (c == '{' or c == '[' or c == '('):
               stack.push(Element(c))               
            elif c == '}' or c == ']' or c == ')':
                if stack.isEmpty != True:
                    c_out = stack.pop()
                    if ((c == '}' and c_out != '{') or
                                ((c == ']' and c_out != '[')) or
                                ((c == ')' and c_out != '(')
                                )): 
                        print "Error, the parenthesis  with no pair"
                        return False
                        
        return True

input1 = "c[d]"
ch1 = CheckParenthesis(input1)
print ch1.check()

input2 = "c[d"
ch2 = CheckParenthesis(input2)
print ch2.check() 

input3 = "a{b[c]d}e"
ch3 = CheckParenthesis(input3)
print ch3.check() 

input4 = "a{b(c]d}e"
ch4 = CheckParenthesis(input4)
print ch4.check()     