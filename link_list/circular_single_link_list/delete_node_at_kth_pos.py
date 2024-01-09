class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def delete_at_head_EA(head):
    if head == None:
        return None
    elif head.next == None:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next 
    
def delte_kth_node(head,k):
    if head == k:
        return delete_at_head_EA(head)

    curr = head

    for i in range(k-2):
        curr = curr.next
    curr.next = curr.next.next
    return head
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
delte_kth_node(head,3)
traverse(head)


