class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def hieght_of_tree(node):
    if node == None:
        return 0
    else:
        h1 = hieght_of_tree(node.left)
        h2 = hieght_of_tree(node.right)
        return max(h1,h2)+1
    

node = Tree(56)
node.left = Tree(78)
node.right = Tree(56)
node.right.right = Tree(53)
# node.right.right.right = Tree(90)
node.left.left = Tree(34)
print(hieght_of_tree(node))