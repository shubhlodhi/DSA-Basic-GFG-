class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def delete_head(head):
    if head == None:
        return None
    if head.next == None:
        return None 

    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    return curr.next
def delete_at_head_EA(head):
    if head == None:
        return None
    elif head.next == None:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next 
    



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
# head = delete_head(head)
delete_at_head_EA(head)

traverse(head)