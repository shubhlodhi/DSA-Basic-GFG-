class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search(head,x):
    
    pos =1
    curr = head
    while curr != None:
        if curr.data == x:
            print(pos)
            return pos
        pos  = pos+1
        curr = curr.next
    return -1

head  = Node(34)
head.next = Node(78)
head.next.next = Node(56)
search(head,34)
        