class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_at_first(head,x):
    temp = Node(x)
    if head == None:
        return None
    if head != None:
        head.prev = temp
        temp.next = head
    return temp
    

def traverse(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
temp = Node(34)
temp1 = Node(78)
temp2 = Node(56)
head = temp
temp.prev  = None
temp.next = temp1
temp.prev = temp
temp1.next = temp2
temp1.prev = temp
# traverse(head)
head = insert_at_first(head,21)
head = insert_at_first(head,29)
traverse(head)
