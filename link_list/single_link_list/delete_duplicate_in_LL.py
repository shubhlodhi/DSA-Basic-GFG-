class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
    
def duplicate(head):
    if head == None:
        return head
    if head.next == None:
        return head
    
    curr = head
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
         curr.next = curr.next.next

        else:
            curr = curr.next
    # return head

def print_LL(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

head = Node(12)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(30)

duplicate(head)
print_LL(head)



