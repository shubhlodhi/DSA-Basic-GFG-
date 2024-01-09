class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
def find_nth(head,n):
    curr = head
    len = 0
    while curr != None:
        curr = curr.next
        len = len + 1
    curr = head
    for i in range(1,len-n+1):
        curr = curr.next
    print(curr.data)

# efficient approach:
def find_nth_EA(head,n):
    first_pointer = head
    for i in range(n):
        first_pointer = first_pointer.next

    second_pointer = head
    while first_pointer != None:
        second_pointer = second_pointer.next
        first_pointer = first_pointer.next
    print(second_pointer.data)
def find_nth_EA(head,n):
    first = head
    for i in range(n):
        first = first.next
    second = head
    while second != None:
        first = first.next
        second = second.next

        print(second.data)




head = Node(12)
head.next = Node(78)
head.next.next = Node(89)
head.next.next.next = Node(45)
head.next.next.next.next = Node(34)
find_nth_EA(head,2)