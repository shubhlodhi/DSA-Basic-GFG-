class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder_trversal(Node):
    if Node != None:
        inorder_trversal(Node.left)
        print(Node.data,end=" ")
        inorder_trversal(Node.right)  # it is a tail recursive (LEFT ,NODE,RIGHT)
def postorder_traversal(Node):
    if Node != None:
        print(Node.data,end=" ")
        inorder_trversal(Node.left)
        inorder_trversal(Node.right) # it is also a tail recursive(NODE,LEFT,RIGHT)
def preorder_traversal(Node):
    if Node!=None:
        preorder_traversal(Node.left)
        preorder_traversal(Node.right)
        print(Node.data,end=" ") # it is not tail recursive(LEFT,RIGHT,NODE)







Node = tree(1)
Node.left = tree(3)
Node.right = tree(8)
Node.left.left =  tree(7)
Node.right.right = tree(9)
# inorder_trversal(Node)
postorder_traversal(Node)
# preorder_traversal(Node)