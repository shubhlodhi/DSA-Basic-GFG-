class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_at_middle(head,data,index):
    temp = Node(data)
    if head == None:
        return temp
    curr = head
    for i in range(index-2):
        curr = curr.next
    temp.next = curr.next 
    curr.next = temp
    return head
def pint_ll(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr =curr.next

head = Node(23)
head.next = Node(67)
head.next.next = Node(78)
insert_at_middle(head,22,3)
pint_ll(head)
