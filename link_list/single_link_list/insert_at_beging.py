class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
def insert_at_first(head,data):
    # curr = head
    temp = Node(data)
    temp.next = head
    # print(temp)
    return temp
    # head.next = None
def pri_LL(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.next
head = None
head = insert_at_first(head,56)
head = insert_at_first(head,78)
head = insert_at_first(head,45)
# insert_at_first(head,23)
pri_LL(head)



    
        