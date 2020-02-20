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
preOrder = Root, left, right
"""
def preOrder(root):
    result = []
    def visit(node):
        # print(node.info, ' ')
        result.append(node.info)

        if node.left is None and node.right is None:
            return

        if node.left:
            visit(node.left)

        if node.right:
            visit(node.right)
            

    visit(root)
    print(' '.join(map(lambda x: str(x), result)))
    #Write your code here

bst = BinarySearchTree()
bst.create(1)
bst.create(2)
bst.create(5)
bst.create(3)
bst.create(4)
bst.create(6)

preOrder(bst.root)

# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
# Iterative function for inorder tree traversal 
def MorrisTraversal(root): 
      
    # Set current to root of binary tree 
    current = root  
      
    while(current is not None): 
          
        if current.left is None: 
            print(current.info)
            current = current.right 
        else: 
            # Find the inorder predecessor of current 
            pre = current.left 
            while(pre.right is not None and pre.right != current): 
                pre = pre.right 
   
            # Make current as right child of its inorder predecessor 
            if(pre.right is None): 
                pre.right = current 
                current = current.left 
                  
            # Revert the changes made in if part to restore the  
            # original tree i.e., fix the right child of predecessor 
            else: 
                pre.right = None
                print(current.info)
                current = current.right 

# Driver program to test the above function 
"""  
Constructed binary tree is 
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
MorrisTraversal(root) 