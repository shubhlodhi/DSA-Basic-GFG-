def left_rotate(arr ,n):
    last_index = arr[n-2]
    first_element = arr[0]
    for i in range(0,n-1):
        arr[i] = arr[i+1]
    arr[last_index] = first_element
    return arr


l = [1,2,3,4]
n  = len(l)
print(l)
left_rotate(l , n)
print(l)