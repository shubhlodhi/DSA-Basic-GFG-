class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def delete_at_first(head):
    if head == None:
        return None
    if head.next == None:
        return None
    head = head.next
    # head.prev = None
    return head
    
def traverse(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
temp = Node(34)
temp1 = Node(78)
temp2 = Node(56)
head = temp
temp.prev  = None
temp.next = temp1
temp.prev = temp
temp1.next = temp2
temp1.prev = temp
head = delete_at_first(head)
traverse(head)
