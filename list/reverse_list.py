def revrse(l , first,end):
    n = len(l)
    last_index = n
    for i in range(n-1,0,-1):
        # l[first] , l[end] = l[end] , l[first]
        l[i] = l[i-1] 
    l[0] = last_index
        
    return l
        # first+=1
        # end-=1
def reverse(arr,start,end):
    if start>=end:
        return 
    else:
        arr[start],arr[end] = arr[end] , arr[start]
        reverse(arr,start+1,end-1)


l = [1,2,3,4,5,6,7]
# n = len(l)
(revrse(l,0,6))
print(l)

    
