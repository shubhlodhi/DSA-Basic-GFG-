# # naive approach:
# def union(arr,arr1):
    
#     a = arr+arr1
#     a.sort()
#     for i in range(0,len(a)):
#         if a[i] != a[i-1]:
            # print(a[i],end=" ")



# effecient approach;
def union(arr,arr1):
    i,j = 0,0
    # temp=  []
    while i<len(arr) and j<len(arr1):
        if i>0 and arr[i] == arr[i-1]:
            i+=1
            # continue
        
        else:
            if j>0 and arr1[j] == arr1[j-1]:
                j+=1
                # continue
        
            else: 
                if arr[i] < arr1[j]:
                    # temp.append(arr[i])
                    print(arr[i])
                    i+=1
                else: 
                    if arr[i]>arr1[j]:
                    #  temp.append(arr1[j])
                     print(arr1[j])
                     j+=1
                    else:
                    #    temp.append(arr[i])
                       print(arr[i])
                       i+=1
                       j+=1
    while i<len(arr):
       if (i>0 and arr[i] != arr[i-1]):
        # temp.append(arr[i])
        print(arr[i])
        i+=1
    while j<len(arr1):
        if (j>0 and arr1[j] != arr[j-1]):
        #  temp.append(arr[j])
         print(arr1[j])
         j+=1

    # return temp
       
                       
    # return temp

a1 = [2,20,20,40]
a2 = [1,10,20]
print(union(a1,a2))



    
    
    