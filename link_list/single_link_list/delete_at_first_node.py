class NOde:
    def __init__(self,data):
        self.data = data
        self.next = None

    # head = None
    # return head

def print_ll(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    # curr = None

def Delete(head):
    # if head == None:
    #     return None
    head = head.next
    return head


    
    # head = None
    
    # return curr
def delete_node_at_last(head):
    if head == None:
        return None
    if head.next == None:
     return None
    
    curr  = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

head = NOde(12)
head.next = NOde(34)
head.next.next = NOde(23)
# print_ll(head)
head = Delete(head)
delete_node_at_last(head)
# delete_node_at_last(head)

print_ll(head)


    





