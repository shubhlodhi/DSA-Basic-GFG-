def naruto_partion(arr ,low,high ,n):
    # n = len(arr)
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <pivot:
            i+=1
            arr[j] ,arr[i] = arr[i] ,arr[j]
    arr[i+1] , arr[high] = arr[high] ,arr[i+1]
    print(arr , "arr")
    return n

n =[10,80,30,90,50,70]
g =len(n)
print(naruto_partion(n,0,g-1,g))

print(n.remove(10))
print(n)
def choco(a,n,m):
    a.sort()
    res =float("inf")
    for i in range(0,n):
        a1  =[]
        for j in range(i,m):
            if m>n:
                break
            a1.append(a[j])
            mini_value = max(a1)-min(a1)
            # print(mini_value)
        res = min(res,mini_value)
        m+=1

    return res
a = [3,4,1,9,56,7,9,12]
n = len(a)
print(choco(a,n,5))
            # min
def negative(a,n):
    j = 0
    for i in range(0,n):
        if a[i] <0:
            a[i] ,a[j] = a[j] , a[i]
            j+=1
        
    return a
def negative1(a,n):
    a1 = []
    for i in range(0,n):
        if a[i]<0:
            a1.append(a[i])
        
    for i in range(0,n):
        if a[i]>0:
            a1.append(a[i]
            )

    return a1

a =[15,-3,-2,10]
n= len(a)
print(negative(a,n))
print(negative1(a,n))
a.sort()
print(a)
# a =[2,3,4]
# aa  =max(a)-min(a)
# print(aa)
def even_odd(a,n):
    a1 =[]
    for i in range(0,n):
        if a[i] %2 == 0:
            a1.append(a[i])

    for i in range(0,n):
        if a[i]%2!=0:
            a1.append(a[i])

    return a1
ar = [10,15,14,13,12,17,13]
n= len(ar)
print(even_odd(ar,n))

def a0_1(a,n):
    j =0
    for i in range(0,n):
        if a[i] == 0:
         a[i] , a[j] = a[j],a[i]
         j+=1

    return a

aw = [0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1]
n =len(aw)
print(a0_1(aw,n))

