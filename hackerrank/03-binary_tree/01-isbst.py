class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_(root): 
    if root is None:
        return True

    left = root.left    
    right = root.right
    data = root.data 
    isBst = True

    if not right and not left:
        return True

    if (right and right.data <= data) or (left and left.data >= data):
        return False

    return isBst and check_binary_search_tree_(left) and check_binary_search_tree_(right)
    
root = Node(100)

root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)

print(check_binary_search_tree_(root))

root = Node(10)

root.left = Node(5)
root.left.left = Node(5)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)
print(check_binary_search_tree_(root))

root = Node(1)
print(check_binary_search_tree_(root))


root = Node(10)

root.left = Node(5)
root.left.left = Node(3)
root.left.right = Node(6)

root.right = Node(13)
root.right.left = Node(11)
root.right.right = Node(18)
root.right.right.right = Node(19)

print(check_binary_search_tree_(root))

root = Node(10)
root.left = Node(5)
root.left.left = Node(4)
root.left.left.left = Node(3)
root.left.left.left.left = Node(2)
root.left.left.left.left.left = Node(1)
root.right = Node(11)
print(check_binary_search_tree_(root))