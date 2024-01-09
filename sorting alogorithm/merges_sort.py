def merege_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merege_sort(left)
        merege_sort(right)
        # return merege(arr,l,h)
# def merege(arr,l,h):
    # mid = (l+h)//2
    
    # left  = arr[l:mid]
    # right  =arr[mid+1:h]
        i,j,k = 0,0,0
        while i<len(left) and j<len(right):
         if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
         else:
        # if left[i] >= right[j]:
            arr[k] = right[j]
            j+=1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr

a = [1,3,2,5,4,6,7]
n = len(a)


print(merege_sort(a))

        



    