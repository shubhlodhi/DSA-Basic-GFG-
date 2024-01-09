import math


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
    def min_xtract(self):
        arr = self.A
        res = arr[0]
        n = len(arr)
        if n == 0:
            return math.inf
        arr[0] = arr[n-1]
        arr.pop()
        self.heapify(0)
        return res
    def heapify(self,x):
        arr = self.A
        smallest = x
        lt = self.left_child(x)
        rt = self.right_node(x)
        n = len(arr)-1
        while n>0:
            if arr[lt] < arr[smallest]:
                smallest = lt
            if arr[rt] < arr[smallest]:
                smallest = rt
            if smallest != x:
                arr[smallest] ,arr[x] = arr[x],arr[smallest]
                self.heapify(smallest)


