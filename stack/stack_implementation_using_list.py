# stack implemne==enataion using list
class Stack:
    def __init__(self):
        self.stack = []
        # self.n = 0

    def push(self ,x):

        return self.stack.append(x)
        # self.n = self.n+1
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def len(self):
        return len(self.stack)
s = Stack()
s.push(34)
s.push(78)
s.push(45)
print(s.pop())
print(s.peek())
print(s.len())
        