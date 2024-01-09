def first_occurence(l,low,high,n):
    if low>high:
        return -1
    mid = (low+high)//2
    # if l[mid] == n:
        # return mid
    
    if l[mid]>n:
            return first_occurence(l,low,mid-1,n)
    else: 
        if l[mid]<n:
            return first_occurence(l,mid+1,high ,n)
        else: 
         if mid==0 or l[mid-1]!=l[mid]:
             return mid
         else:
             return first_occurence(l,low,mid-1,n) 
def last_occurence(l,low,high,n):
    if low>high:
        return 1
    mid = (low+high)//2
    if l[mid]>n:
        return last_occurence(l,low,mid-1,n)
    else:
        if l[mid]<n:
            return last_occurence(l,mid+1,high,n)
        else:
            if mid == len(l)-1 or l[mid]!=l[mid+1]:
                return mid
            else:
                return last_occurence(l,mid+1,high,n)


def ocuurence(l,low,high,x):
    first = first_occurence(l,low,high,x)
    if first == -1:
        return 0
    else:
        return last_occurence(l,low,high,x) - first+1
    
l = [1,2,3,4,5,5,5,5,5]
print(ocuurence(l,0,len(l) , 5))