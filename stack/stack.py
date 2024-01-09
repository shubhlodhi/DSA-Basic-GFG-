# stack implmentaio using linked_list.
import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):

        self.head = None
        self.n = 0
    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.n = self.n+1
        # print(temp)
        return temp
    def len(self):
        return self.n
    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data
    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.n = self.n-1
        return res
    # def traverse(self):
    #     curr = self.head
    #     while curr != None:
    #         print(curr.data)
    #         curr = curr.next
        
S = Stack()

S.push(21)
S.push(23)
S.push(67)
print(S.peek())
print(S.pop())
print(S.len())
# S.traverse()