class Node:
    def __init__(self,data):
        self.data  = data
        self.next  = None
def insert_at_first(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    # temp.next= head
    curr.next = temp
    temp.next = head
    # curr.next = temp
    return temp
def insert_at_first_EA(head,x):
    temp =Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        # head.next = temp
        temp.next = head.next
        head.next = temp
        head.data , temp.data = temp.data , head.data


def traverse(head):

    if head == None:
        return
        
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

head = Node(78)
head.next = Node(223)
head.next.next = Node(67)
head.next.next.next = head
# head = insert_at_first(head,45)
# traverse(head)
insert_at_first_EA(head,45)
traverse(head)