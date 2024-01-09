def find_pair(arr,n,x):
    hash = x%n
    i  =0
    while i<n:
        if arr[hash] + arr[i] == x:
            return 1
        
        hash = +1

a = [1,2,3,4,5]
n = len(a)
print(find_pair(a,n,6))

        
