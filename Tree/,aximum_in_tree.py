import math


class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def maximum(node):
    if node ==None:
        return -math.inf
    else:
        lm = maximum(node.left)
        rm = maximum(node.right)
        return max(node.data , lm,rm)



node = Tree(56)
node.left = Tree(78)
node.right = Tree(56)
node.right.right = Tree(53)
# node.right.right.right = Tree(90)
node.left.left = Tree(34)
print(maximum(node))
