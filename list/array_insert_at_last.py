def insert_array(arr ,sizeofarray, element):
    # for i in range(0,n):
    if len(arr)<sizeofarray:
        s = arr.append(element)
        # arr[n-1] = element
    else: 
        return " array is full"
l = [1,2,3,4]
n = len(l)
print(insert_array(l,4,12))
print(l)