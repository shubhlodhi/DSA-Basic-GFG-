# def search(l,low,high,x):
#     mid = (low+high)//2
#     if l[mid] == x:
#         return mid
#     if l[mid]>x:
#         return search(l,low ,mid-1,x)
#     if l[mid] <x:
#         return search(l,mid+1,high,x)
    
# l = [1,2,3,4,5,6,7]


# print(search(l,0,len(l),5))


def binary_search_iterative_approach(l,low,high,x):
    mid = (low+high)//2
    while low<high:
     if l[mid] ==x:
        return mid
     elif l[mid]>x:
        high = mid-1
     else:
        low = mid+1
    return -1
l = [1,2,3,4,5]
print(binary_search_iterative_approach(l,0,len(l) ,5))

