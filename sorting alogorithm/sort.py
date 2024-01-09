# print(l)
def myfun(s):
    return (s)
l =[1,3,4,2,5]
l.sort()
# l1 = l.sorted()
print(l)

l.sort(key=myfun)
# l.sort(key=myfun , reverse=True)
print(l)