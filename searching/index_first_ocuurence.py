def binary(l,low,high,n):
    if low>high:
        return -1
    mid = (low+high)//2
    # if l[mid] == n:
        # return mid
    
    if l[mid]>n:
            return binary(l,low,mid-1,n)
    else: 
        if l[mid]<n:
            return binary(l,mid+1,high ,n)
        else: 
         if mid==0 or l[mid-1]!=l[mid]:
             return mid
         else:
             return binary(l,low,mid-1,n) 
         

def Iterative_approach(l,low,high,n):
    mid = (low+high)//2
    while low<high:
        # if l[mid]==n:
            # return mid
        if l[mid]>n:
            high = mid-1
        elif l[mid]<n:
            low = mid+1

        else:
            if mid ==0 or l[mid-1] != l[mid]:
                return mid
            else:
                high = mid-1
            
l = [1,2,3,3,4,4,5,5]
print(Iterative_approach(l,0,len(l),4))