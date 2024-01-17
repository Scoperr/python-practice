class node:
    def __init__(self, left = None, right = None, key=0):
        self.key = key
        self.left = None
        self.right = None
class tree:
    def __init__(self,key):
        self.root = node(key=key)
    def display(self, temp):
        if temp == None:
            return
        else:
            #print(temp.key)
            self.display(temp.left)
            print(temp.key)
            self.display(temp.right)
            #print(temp.key)
    def insert_right(self, key):
        pass
    def insert_left(self, key):
        pass
tree1 = tree(key=4)
n1 = node(key=2)
tree1.root.left = n1
n2 = node(key=5)
tree1.root.right = n2
n3 = node(key=7)
n2.left = n3
n2.right = node(key=9)
tree1.display(tree1.root)