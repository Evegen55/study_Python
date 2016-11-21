"""
Now try implementing a BST on your own. You'll use the same Node class as before:

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
This time, you'll implement search() and insert(). You should rewrite search() 
and not use your code from the last exercise so it takes advantage of BST properties. 
Feel free to make any helper functions you feel like you need, including the print_tree() function 
from earlier for debugging. You can assume that two nodes with the same value won't be inserted into the tree. 

Beware of all the complications discussed in the videos!
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        newNode = Node(new_val)
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            parent = Node(None)
            while True:
                parent = current
                if new_val < current.value:
                    current = current.left
                    if current is None:
                        parent.left = newNode
                        return
                else:
                    current = current.right
                    if current is None:
                        parent.right = newNode
                        return      

    def search(self, find_val):
        current = self.root
        while current.value != find_val:
            if find_val < current.value:
                current = current.left
            else:
                current = current.right
            if current is None:
                return False
        return True
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
# Should be True
print tree.search(5) #implement insert method