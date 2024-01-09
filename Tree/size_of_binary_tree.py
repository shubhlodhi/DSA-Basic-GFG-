class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def size(node):
    if node == None:
        return 0
    else:
        l1 = size(node.left)
        l2 = size(node.right)
        return (l1+l2)+1

node = Tree(56)
node.left = Tree(78)
node.right = Tree(56)
node.right.right = Tree(53)
# node.right.right.right = Tree(90)
node.left.left = Tree(34)
print(size(node))