class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    def visit(node):
        if node.left is None and node.right is None:        
            return

        if node.left:
            visit(node.left)
            print(node.left.info, end=' ')   

        if node.right:
            visit(node.right)
            print(node.right.info, end=' ')   

    visit(root)
    print(root.info, end=' ')
    #Write your code here

tree = BinarySearchTree()
tree.create(1)
tree.create(2)
tree.create(5)
tree.create(3)
tree.create(6)
tree.create(4)

postOrder(tree.root)