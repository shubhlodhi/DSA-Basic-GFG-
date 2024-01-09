class node:
    def __init__(self):
        self.A= []
    def parent_node(self,i):
        return (i-1)//2
    def right_node(self,i):
        return (2*i+1)
    def left_child(self,i):

        return (2*i+2)
    def insert(self,x):
        arr = self.A
        arr.append(x)
        i = len(arr)-1
        while i>0 and arr[self.parent_node(i)] > arr[i]:
            p = self.parent_node(i) 
            arr[i] ,arr[p] = arr[p],arr[i]
            i = p
        return arr
    def level_order(self,node):
        s = self.A
        s.append(node)
        i =0
        while len(s)>0:
            s[node] = s.pop(0)
            print(s[node])
            if s[self.left_child(i)] is not None:
                s.append(self.left_child[node])
            if s[self.right_node(i)] is not None:
                s.append(self.right_node[node])
        return s
    def decrease_key(self,i,x):
        arr = self.A
        arr[i] = x
        # n = len(arr)-1
        while i>0 and arr[self.parent_node(i)] > arr[i]:
            p = self.parent_node(i)
            arr[p] , arr[i] = arr[i] , arr[p]
            i =p
            



        
s = node()
s.insert(12)
s.insert(34)
s.level_order(0)    
