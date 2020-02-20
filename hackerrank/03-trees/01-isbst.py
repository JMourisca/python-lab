 # Tree is a hierarchical data structure. Main uses of trees include maintaining hierarchical data, 
 # providing moderate access and insert/delete operations. 
 # Binary trees are special cases of tree where every node has at most two children.

 # Maximum number of nodes in level L (root = level 1): 2^(L-1)
 # Maximum number of nodes in a binary tree of heigh H (root = height 1): 2^H - 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# https://www.techseries.dev/products/coderpro/categories/1831147/posts/6231427
# Time: O(n)
# Space: O(n)
def check_binary_search_tree_(root): 
    def check_binary_search_tree(node, lower, upper):
        if not node:
            return True

        data = node.data
        isBst = True

        if data <= lower or data >= upper:
            return False

        if not check_binary_search_tree(node.right, data, upper):
            return False
        
        if not check_binary_search_tree(node.left, lower, data):
            return False
        return True

    return check_binary_search_tree(root, float("-inf"), float("inf"))
    

root = Node(100)

root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)

print(check_binary_search_tree_(root) == False) # false

root = Node(10)

root.left = Node(5)
root.left.left = Node(5)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)
print(check_binary_search_tree_(root) == False) # false

root = Node(1)
print(check_binary_search_tree_(root) == True) # true

root = Node(10)

root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)
root.right.right.right = Node(19)

print(check_binary_search_tree_(root) == True) # true

root = Node(10)
root.left = Node(5)
root.left.left = Node(4)
root.left.left.left = Node(3)
root.left.left.left.left = Node(2)
root.left.left.left.left.left = Node(1)
root.right = Node(11)
print(check_binary_search_tree_(root) == True) # true

root = Node(10)

root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(9)
root.right.right = Node(18)
root.right.right.right = Node(19)

print(check_binary_search_tree_(root) == False) # false