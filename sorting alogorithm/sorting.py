# class sorted:
#     def __init__(self ,x,y):
#         self.x =x
#         self.y= y
# def myfun(p):
#         return p.x
    
# s = [sorted(1,18) , sorted(2,18) ,sorted(3,4)]

# s.sort(key=myfun)
# for i in s:
#      print(i.x ,i.y)


class sorting:
     def __init__(self,x,y):
          self.x = x
          self.y = y
     def __lt__(self,other):
        if self.x == other.x:
             return self.y<other.y
        else:
             return self.x<other.x

l = [sorting(1,13) , sorting(4,34) , sorting(1,1)]
l.sort()
for i in l:
     print(i.x,i.y)    
