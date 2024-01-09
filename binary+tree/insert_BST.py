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
def iterative_insert(node,data):
    parent = None
    curr = node
    while curr != None:
        parent = curr
        # if curr == None:
        #     return bst(data)
        if curr.data == data:
            return node
        elif curr.data > data:
            curr = curr.left
        else:
        # elif curr.data < data:
            curr = curr.right

    if parent == None:
                return bst(data)
    elif parent.data > data:
         parent.left = bst(data)
    else:
         parent.right = bst(data)

    return node
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
iterative_insert(node,44)
iterative_insert(node,99)
level_order(node)