def Iterative_Approach(l,low,high,n):
    # if low>high:
        # return 1 
    
    while low<=high:
        mid = (low+high)//2
        if l[mid]>n:
            high = mid -1
        else:
            if l[mid]<n:
                low = mid+1
            else:
                if mid == (len(l)-1) or l[mid] != l[mid+1]:
                    return mid
                else:
                    low = mid+1

l = [1,1,2,2,3,4,4,4,5]
print(Iterative_Approach(l,0,len(l),4))


def recursive_approach(l,low,high,n):
    if low>high:
        return 1
    mid = (low+high)//2
    if l[mid]>n:
        return recursive_approach(l,low,mid-1,n)
    else:
        if l[mid]<n:
            return recursive_approach(l,mid+1,high,n)
        else:
            if mid == len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                return recursive_approach(l,mid+1,high,n)


l = [1,1,2,3,4,4,4,4,5]
print(recursive_approach(l,0,len(l) , 4))
         