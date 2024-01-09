def buuble_sort(l,n):
    sorted = False
    for i in range(n-1):
     for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j] ,l[j+1] = l[j+1] ,l[j]
    #  return l
            sorted = True
    if sorted == False:
        return
    return l
   

l = [1,4,72,5,3,5]
n =len(l)
print(buuble_sort(l,n))
\


def bubble_sort(arr,n):
    for i in range(0,n-1):
        sorted =  False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
            sorted = True
        if sorted == False:
            break
    return l

