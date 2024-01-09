from collections import deque

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
def print_k_pos(node,k):
    if node == None:
        return
    elif k == 0:
        print(node.data,end=" ")
    else:
        print_k_pos(node.left,k-1)
        print_k_pos(node.right,k-1)
    
def level_order_traversal(node):
    h = hieght_of_tree(node)
    for i in range(h):
        print_k_pos(node,i)  
#  time complexity = O(N+nh) = O(NH)
# QUEUE data STRUCTURE for effiecent approach:

def level_order_traversal_EA(node):
    if node ==None:
        return
    q = deque()
    q.append(node)
    while len(q)>0:
        node = q.popleft()
        print(node.data)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
def levele_order_traversal_using_list(node):
    if node == None:
        return
    s  =[]
    s.append(node)
    while len(s)>0:
        node = s.pop(0)
        print(node.data)
        if node.left is not None:
            s.append(node.left)
        if node.right is not None:
            s.append(node.right)

# it take O(N) time to complete the popo operation thats why we use deque operation 

    

    






node = Tree(56)
node.left = Tree(78)
node.right = Tree(57)
node.right.right = Tree(53)
node.right.right.right = Tree(90)
node.left.left = Tree(34)
# print(hieght_of_tree(node))
# level_order_traversal(node)
# level_order_traversal_EA(node)
levele_order_traversal_using_list(node)