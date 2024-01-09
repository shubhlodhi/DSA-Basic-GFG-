def inversion(arr ,n  ):
    pivot = arr[3]
    arr[pivot] , arr[n-1] = arr[n-1] ,arr[pivot]
    temp =[]


    for i in arr:
        if i <= pivot:
            temp.append(i)
    for i in arr:
        if i >= pivot:
            temp.append(i)

    
    # 
    # arr[i] = temp[i]
    return temp


a = [1,2,5,3,6,78]
n =len(a)
print(inversion(a ,n))




     