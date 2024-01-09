def delete_index(arr,n,index):
    # temp = [0]*n
    if index<0:
        return 1

    # last_index = 0
    for i in range(index,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = 0
        # return index

l = [1,2,3,4,5]
n = len(l)
delete_index(l,n,2)
print(l)