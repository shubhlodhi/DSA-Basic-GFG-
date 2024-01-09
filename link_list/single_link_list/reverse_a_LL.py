class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
def print_LL(head):
    curr = head
    while curr  != None:
        print(curr.data)
        curr = curr.next
head = Node(12)
head.next = Node(78)
head.next.next = Node(89)
head.next.next.next = Node(45)
head.next.next.next.next = Node(34)
# print_LL(head)

reverse(head)
print_LL(head)



