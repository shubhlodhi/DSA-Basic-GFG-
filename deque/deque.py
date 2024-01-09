from collections import deque
# with the help of deque we perform insert and delete operation in a constant time
# we can acces the elements from both side rear and front 
# perferm operation like given below:
s = deque()
s.append(12)
s.append(45)
s.appendleft(56)
# print(s)
print(s.count(12))
s.insert(2,78)
print(s)
print(s.pop())
print(s)
s.popleft()
print(s)
s.extend([67,78]) # it adds the elements in the last of the queue
print(s)
s.extendleft([78,34]) # extend function used to add the elemnets in the left of deque 
print(s)
s.rotate(2)  # it uses to rotate in a clockwise
print(s)
s.rotate(-2) # it uses to rotate in a anti-clockwise
print(s)
s.reverse() # use to reverse the deque
print(s)
print(s[0])
print(s[-1])
s[2] = 100 # add elements in a given position 
print(s)

#  in deque slicing is not possible