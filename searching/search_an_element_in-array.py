def binary(arr,n,low,high,x):
    if x == 0:
        return 0
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    else:
        if arr[mid] > x:
            return binary(arr,n,low,mid+1,x)
        else:
            return binary(arr,n,mid+1,high,x)
        
arr = [1,2,3,4,5,6]
n = len(arr)
print(binary(arr,n,0,n-1,5))


def square_root(n):
    i =1
    while i*i<=n:
        i+=1
    return i-1

print(square_root(4))
