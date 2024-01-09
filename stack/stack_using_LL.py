# import math
# class Node:
#     def __init__(self,data):
#         self.data  = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.n = 0
#     def push(self,x):
#         temp = Node(x)
#         temp.next = self.head
#         self.head = temp
#         self.n = self.n+1
#         return temp
    
#     def peek(self):
#         if self.head == None:
#             return math.inf
#         # return self.head.data
#         return self.head.data
#     def pop(self):
#         res = self.head.data        
#         self.head = self.head.next
#         self.n = self.n-1
#         return res
#     def len(self):
#         return self.n
class Stack:
    def __init__(self):
        self.stack = []
        self.n =0
    def push(self,x):
        return self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def len(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]

    
        
s = Stack()
s.push(23)
s.push(67)
s.push(65)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.len())
    