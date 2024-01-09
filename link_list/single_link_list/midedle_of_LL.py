class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def find_middle(head):
    curr = head
    count = 0
    while curr != None:
        count = count +1
        curr = curr.next
        # print(count)

    curr  = head
    # print(curr.data)
    for i in range(count//2):
        curr = curr.next
    print(curr.data)
# efficient_approach:
def find_middle_EA(head):
    curr = head
    s_curr = head

    while s_curr.next != None:
        curr = curr.next
        s_curr = s_curr.next.next
    print(curr.data)

def print_LL(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

    
head = Node(12)
head.next = Node(78)
head.next.next = Node(89)
head.next.next.next = Node(45)
head.next.next.next.next = Node(34)
find_middle_EA(head)
