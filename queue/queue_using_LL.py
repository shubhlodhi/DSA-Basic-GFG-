class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n =0
    def get_size(self):
        return self.n
    def get_front(self):
        return self.front.data
    def get_rear(self):
        return self.rear.data
    def enque(self,x):
        temp = Node(x)
        if self.rear ==None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            # if self.front == None:
                # self.rear = None
            self.rear=temp  
            self.n = self.n+1

       
       

    def deque(self):
        if self.front == None:
            return None
        else:
         res = self.front.data
         self.front = self.front.next
         if self.front ==None:
            self.rear =None
         self.n = self.n-1
         return res

d = queue()
d.enque(45)
d.enque(78)
d.enque(56)
print(d.deque())
print((d.get_front()))
# print(d.get_rear())



        