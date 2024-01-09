class Deque:
 def __init__(self,C):
  self.L = [None]*C
  self.c = C
  self.n = 0
  self.front = 0
  self.rear = (+1)%self.c
 def push_in_front(self,x):
  self.front = (self.front-1)%self.c
  self.L[self.front] = x
  self.n = self.n+1
#   return self.front

 def push_in_rear(self,x):
  self.rear = (self.front-self.n)%self.c 
  self.L[self.rear] = x
  self.n =self.n-1
#   return self.rear
 def delete_in_front(self):
  res = self.L[self.front]
  self.front = (self.front+1)%self.c
  self.n = self.n-1
#   new_front = self.L[new_front]
  return res
 def print_L(self):
  for i in range((self.c)):
   print(self.L[i])
 def delete_in_rear(self):
  res = self.L[self.rear]
  self.rear = (self.rear-1)%self.c
  self.n = self.n-1
  return res


 

s = Deque(4)
s.push_in_front(12)
s.push_in_front(45)
s.push_in_rear(76)
s.push_in_rear(34)
print(s.delete_in_front())
print(s.delete_in_rear())
print(s.delete_in_rear())
# print(s.delete_in_front())
# print(s.delete_in_front())
# s.print_L()


