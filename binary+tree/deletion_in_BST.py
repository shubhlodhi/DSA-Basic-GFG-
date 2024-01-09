class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def insert(node,data):
    
    # Node = node(data)
    if node == None:
        return bst(data)
    if node.data == data:
        return node
    elif node.data > data:
        node.left = insert(node.left,data) # here node.left varibale is important factor becoz it connect the node from its parent node
    else:
        node.right = insert(node.right,data) # same here node.right
    return node
def delete_Node(node,key):
    if node == None:
        return
    # if node.data == key:
    #     if node.left == None:
    #         return node.right
    #     if node.right == None:
    #         return node.left
    #     else:
    #         return None
    if node.data > key:
        node.left = delete_Node(node.left,key)
    elif node.data <key:
        node.right = delete_Node(node.right,key)
    else:
        if node.left == None:
             return node.right
        if node.right == None:
             return node.left
        else:
             succ = inorder_successor(node.right,key) 
             node.data = succ
             node.right = delete_Node(node.right,succ)
    return node
def inorder_successor(node,k):
    while node.left != None:
        node = node.left
    return node.data
def level_order(node):
    if node ==None:
        return None
    l =[]
    l.append(node)
    while len(l)>0:
        node = l.pop(0)
        print(node.data, end=" ")
        if node.left is not None:
            l.append(node.left)
        if node.right is not None:
            l.append(node.right)
        

node = bst(78)
node = (insert(node,12))
node = insert(node,90)
insert(node,89)
insert(node,67)
# iterative_insert(node,44)
# iterative_insert(node,99)
delete_Node(node,78)
level_order(node)
