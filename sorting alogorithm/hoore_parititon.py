def hoore_partiton(arr,low,high):
    pivot = arr[low]
    i = low-1
    j = high+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i] ,arr[j] = arr[j] ,arr[i]
    
        # print(arr)
        # return arr

    # return arr
def prin_array(arr,n):
    for i in range(0,n):
        print(arr[i] , end=" ")
def deffiernce(a,n):
    res = float("inf")
    for i in range(0,n):
        for j in range(i+1,n):
            diff = abs(a[i]-a[j])  #abs is used to convert negative number to positive 
            # if diff < 0:
            #  break 
                
            res = min(res,diff)
    return res
a =[1,8,12,5,18]
n = len(a)
print(deffiernce(a,n))


# a = [5,3,8,4,2,7,1,10]
# n = len(a)
# print(hoore_partiton(a,0,n-1))
# prin_array(a,n)





    
