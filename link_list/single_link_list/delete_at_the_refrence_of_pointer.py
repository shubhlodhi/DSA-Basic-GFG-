class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

def delte_at_pointer(pointer):
    temp = pointer.next
    pointer.data = temp.data
    pointer.next = temp.next 
    return temp

def print_ll(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next


head = Node(90)
head.next = Node(67) 
head.next.next = Node(34)
delte_at_pointer(head.next)
print_ll(head)

