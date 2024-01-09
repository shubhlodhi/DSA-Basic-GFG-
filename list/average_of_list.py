# l = [12,13,14,15,16,16]
# sum= 0
# for i in l:
#     sum = sum + i
# h=sum//len(l)

# print(h)


def immediateSmaller(arr,n,x):
        smaller = None
        for i in range(n):
            if arr[i] != x:
                if smaller is None or arr[i]<x:
                    smaller = arr[i]
                else:
                    smaller = min(smaller,arr[i])
        return smaller
a = [1 ,5,3, 4, 5]
n =len(a)
print(immediateSmaller(a,n,1))
