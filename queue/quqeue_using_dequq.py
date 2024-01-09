from collections import deque

s = deque()
s.append(12)
s.append(78)
s.append(34)
s.append(78)
print(s)
s.popleft()
print(s)
# deque takes constant time to perform a dequq operation.