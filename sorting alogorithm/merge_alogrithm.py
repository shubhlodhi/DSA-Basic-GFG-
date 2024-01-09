


# a1 = [1,2,3,8]
# a2 = [5,6,7,4]
# print(merge(a1,a2))


def merege_sort(arr,l,h):
    if h>l:
        # return 
       mid = (l+h)//2
    #    left = arr[:mid]     # merege_sort(arr,l,mid+1)
    #    right = arr[mid:]    # merege_sort(arr,mid+1 ,h)
       left = merege_sort(arr,l,mid)
       right  = merege_sort(arr ,mid+1,h)
       return merge(left,right)
def merge(arr1,arr2):
    i = j =0
    n1 = len(arr1)
    n2 = len(arr2)
    new_arr = []
    while i<n1 and j<n2:
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i+=1
        else:
            new_arr.append(arr2[j])
            j+=1

    while i<n1:
        new_arr.append(arr1[i])
        i+=1
    while i<n2:
        new_arr.append(arr2[j])
        j+=1
    return new_arr
# def printList(arr):
    # for i in range(len(arr)):
        # print(arr[i], end=" ")
    # print()

a = [1,32,5,4,6,7]
n = len(a)
# print(printList(a ))
print(merege_sort(a ,0,n-1))
# print(printList(a))


    

