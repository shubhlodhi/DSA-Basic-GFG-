class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def sorted_insert(head,x):
    temp = Node(x)
    if head == None:
        return temp
    if head.data > temp.data:
        temp.next = head
        return head
    curr = head
    while curr.next != None and curr.next.data < x:
        curr = curr.next
   
    temp.next = curr.next
    curr.next = temp
    return head
def print_ll(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
sorted_insert(head,3)
print_ll(head)
        
