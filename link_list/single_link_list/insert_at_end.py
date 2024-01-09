class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_at_end(head,data):
    curr = head
    while curr.next != None:
        curr  =curr.next
    temp = Node(data)
    curr.next = temp
    return head
def pir_ll(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

head = Node(21)
head.next = Node(56)
insert_at_end(head,22)
insert_at_end(head,78)
pir_ll(head)
