class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Search(Node,data):
    if Node == None:
        return False
    if Node.data == data:
        return True
    # else:
    elif Node.data < data:
            return Search(Node.right , data) 
    else:
            return Search(Node.left,data)

Node = BST(10)
Node.left = BST(15)
Node.right = BST(30)
Node.left.left = BST(5)
Node.right.right = BST(50)
Node.left.right = BST(25)
Node.right.left = BST(20)
print(Search(Node,22))

