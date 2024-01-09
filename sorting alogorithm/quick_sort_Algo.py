# from hoore_parititon import hoore_partiton
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
def quick_sort(arr,low,high):
    # mid  =(low+high)//2
    if low<high:
        mid = hoore_partiton(arr,low,high)
        quick_sort(arr,low,mid)
        quick_sort(arr,mid+1,high)
    # return arr
# a  =[1,4,2,5,2,7,6]
# print(quick_sort(a,0,len(a)))
        
def printArray(arr, n): 
    for i in range(n): 
        print(arr[i], end=" ") 
    # print() 
  
  

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr, 0, n - 1) 
print("Sorted array:") 
printArray(arr, n)     