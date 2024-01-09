class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_recursive(head):
    if head == None:
        return None
    if head.next == None:
        return head


    rest_head = reverse_recursive(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return head

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

# reverse_recursive(head)
print_LL(head)