def serach_binary(n,element,low,high):
    mid = (low+high)//2 
    if n[mid] == element:
        return mid
    if n[mid] > element:
        return serach_binary(n,element,low,mid-1)
    else:
        return serach_binary(n,element,mid+1,high)
n = [1,2,3,4,5]
a = len(n)
print(serach_binary(n,4,0,a-1))

def searchInSorted(arr, N, K):
        if arr[N] == K:
            return N
        else:
            return searchInSorted(arr,N-1,K)


n = [1,2,3,4,5]
a = len(n)-1
print(searchInSorted(n,a,2))

def search(arr,N,K):
     for i in range(N):
          if arr[i] == K:
               return i
          
     return 0
          
# a = [1,2,3,4,5]
# n = len(a)
# print(search(a,n,2))

# def left_most(arr,n,k):
#      for i in range(n):
#           if arr[i] == k:
#                return 
          
# def peak(arr,n):
#      if arr[0] > arr[1]:
#           return arr[0]
#      if arr[n-1] > arr[n-2]:
#           return arr[n-1]
#      for i in range(1,n):
#           if arr[i] > arr[i+1]:
#                return arr[i]
          
#      return -1

# arr = [1,2,1,4,1]
# n= len(arr)
# print(peak(arr,n))

# def binary_peak(arr,n):
#      low=0
#      high = n-1
     
#      while low<high:
#        mid = (low+high)//2
#        if (mid==0 or arr[mid]>arr[mid-1]) and(mid==n-1 or arr[mid]>arr[mid+1]) :
#             break
#        if mid >= 0 and arr[mid]<arr[mid-1]:
#             high = mid-1
#        else:
#             low = mid+1

def count_1s(arr,n):
     for i in range(n):
          if arr[i] == 1:
               return i
          
def countlast(arr,n):
     for i in range(n-1,0,-1):
          if arr[i] == 1:
               return i


def count(arr,n):
     if n == 0:
          return -1
     else:
          return (countlast(arr,n) - count_1s(arr,n) +1)
     


arr = [0,0,1,1,1,1,1]
n= len(arr)
# print(count_1s(arr,n))
print(countlast(arr,n))
print(count(arr,n))


          
def floor_using_binary_serach(arr,n ,k):
     low = 0
     high =n-1
     # res = 0
    
     while low<high:
          mid = (low+high)//2
          if arr[mid] == k:
               return arr[mid]
          if arr[mid-1] <k and arr[mid]>k:
               return arr[mid-1]  
          if arr[mid]> k:
               # res = arr[mid]
               
               high = mid-1
          else:
               
               low = mid+1

     return -1

     
     

a = [1 ,2 ,8,10, 11, 12, 19]
n = len(a)
print(floor_using_binary_serach(a,n,5))









               
            


     
          


          
     