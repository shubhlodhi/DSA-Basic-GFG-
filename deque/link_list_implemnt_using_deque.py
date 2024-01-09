#  we use dobly linked list for perfomr operation in a constant time but if we use the sinlge link list we do not able perform like 
# delete  at the end operation in a constant time so that why we use doubly link list for cintant time operation
# we perfomr operation like insert and delete in first and insert at end perfrom in a constant time
class DLL:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.n  = 0
    def push_in_rear(self,x):
        temp = DLL(x)
        if self.rear == None:
            self.front = temp 
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.n = self.n+1
    def push_in_front(self,x):
        temp = DLL(x)
        if self.front == None:
            return None
        temp.next = self.front
        self.front.prev = temp
        self.front = temp
        self.n = self.n+1
        
        return temp

    def delete_in_front(self):
        if self.front == None:
            return None
        else:
            res = self.front.data            
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.front.prev = None
            self.n = self.n-1
            return res
    def delete_in_rear(self):
        if self.front == None:
            return None
        else:
            res = self.rear.data
            self.rear.prev = self.rear
            self.rear.next = None
            return res



            




