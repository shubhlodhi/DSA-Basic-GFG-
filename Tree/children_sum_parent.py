from collections import deque


class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def child_parent_sum(node):
    if node == None: 
        return
    s = deque()
    s.append(node)
    res = 0
    while len(s)>0:
        node = s.popleft()
        if node.left != None:
            a = node.left.data
        else:
            a = 0
            
        if node.right != None:
             b = node.right.data
            
        else:
            b=0
        if a + b == node.data:
            res+=1
    return res



node = Tree(56)
node.left = Tree(56)
# node.right = Tree(6)
# node.right.right = Tree(53)
# node.right.right.right = Tree(90)
# node.left.left = Tree(34)
print(child_parent_sum(node))