class Node:
    def __init__(self,key):
        self.data = key
        self.next = None
def pri_LL(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.next
# temp1 = Node(22)
# temp2 = Node(44)
# temp3 = Node(89)
# head = temp1
# temp1.next = temp2
# temp2.next = temp3
head = Node(21)
head.next = Node(22)
head.next.next = Node(45)
pri_LL(head)

