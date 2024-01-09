class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):

    if head == None:
        return None
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

head = Node(78)
head.next = Node(223)
head.next.next = Node(67)
head.next.next.next = head

traverse(head)
