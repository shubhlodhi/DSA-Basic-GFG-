class Node:
    def __init__(self,data):
        self.data  = data
        self.next  = None

def insert_at_last(head , x):
    temp = Node(x)
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return head
def insert_at_last_EA(head,x):
    temp = Node(x)
    if head.next == None:
        return temp
    else:
        temp.next = head.next
        head.next = temp
        temp.data , head.data = head.data , temp.data
        return temp
    


    
    
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
# insert_at_last(head,6)
head = insert_at_last_EA(head,6)
traverse(head)