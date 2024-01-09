def left_index(arr,n,low,high,x):
    if n == 0:
        return 0
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    else:
        if arr[mid] >x:
            return left_index(arr,n,low,mid-1)
        else:
            if arr[mid]<x:
                return left_index(arr,n,mid+1,high)
            else:
                if mid == 0 or arr[mid-1] != arr[mid]:

                   
                    return mid
                else:
                    return left_index(arr,n,low,mid-1)
                
arr = [1,2,3,4,5,5,5,6,7]
n= len(arr)
print(left_index(arr,n,0,n-1,5))
