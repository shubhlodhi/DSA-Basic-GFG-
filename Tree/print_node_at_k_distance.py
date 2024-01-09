class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_k_pos(node,k):
    if node == None:
        return
    elif k == 0:
        print(node.data,end=" ")
    else:
        print_k_pos(node.left,k-1)
        print_k_pos(node.right,k-1)
node = Tree(56)
node.left = Tree(78)
node.right = Tree(56)
node.right.right = Tree(53)
# node.right.right.right = Tree(90)
node.left.left = Tree(34)
print_k_pos(node,2)