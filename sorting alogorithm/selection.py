def selection_Sort(l,n):
   
        

    for i in range(n-1):
        min = i
        # print(min)
        

        for j in range(i+1,n):
            if l[j] < l[min]:
                min = j
                # print(l[min])
            
                l[min] , l[i] = l[i] , l[min]
            # l[min] , l[i] = l[i] , l[min]
            
    return l



l = [1,2,4,5,6,3]
n = len(l)
print(selection_Sort(l,n))
# it is not a stable sorting the indexing value is not sort according to a increasing order.
def selection_sort(arr,n):
    for i in range(n-1):
        min = i
        
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
            l[min] ,l[i] = l[i] ,l[min]
        return l
            

