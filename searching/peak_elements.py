def peak(arr,n):
    # peak = 0
    if n==0:
            return 0
    if arr[0] > arr[1]:
            return 0
    if arr[n-1] > arr[n-2]:
            return n-1
        
    
    for i in range(1,n):
           if arr[i] > arr[i+1] and arr[i]>arr[i-1]:
                  return i

    # return i
arr = [1,2,4,5,2]
n =len(arr)
print(peak(arr ,n))


# def peak_elements(arr ,n):
#        low =0
#        high = n-1
#        while low<=high:
#               mid = (low+high)//2
#               if ((mid == 0 or arr[mid-1]<=arr[mid]) and (mid == n-1 or arr[mid+1]<=arr[mid])):
#                      break
              
#               elif mid > 0 and arr[mid-1]>arr[mid]:
#                             high = mid-1
#               else:
#                             low = mid+1
#        return mid
        
# arr = [1,2,3,4,53,3,2]
# n= len(arr)
# print(peak_elements(arr,n))
# recursive approach

# def peak(arr,n):
#     if n == 0:
#         return 0
#     if arr[0] > arr[1]:
#         return 0
#     if arr[n-1]>arr[n-2]:
#         return n-1
#     for i in range(1,n):
#         if arr[i] > arr[i+1] and arr[i]>arr[i-1]:
#             return i


# arr = [1,2,3,4,5,33,2]
# n = len(arr)
# print(peak(arr,n)) 

# # uterative_aoprioach: using binary serach
# def iterative_approach(arr,n):
#     low =0
#     high =n-1
#     while low<=high:
#         mid = (low+high)//2
#         if (mid == 0 or arr[mid-1] <=arr[mid]) and (mid == n-1 or arr[mid+1] <=arr[mid]):
#             break
#         elif (mid >0 and arr[mid-1]>arr[mid]):
#             high = mid-1
#         else:
#             low = mid+1

#     return mid


# arr = [1,2,3,44,4]
# n= len(arr)
# print(iterative_approach(arr,n))

# recursive_approach:
# def recursive_method(arr,n,l,h):
#     if l>=h:
#         return 0
    
#     mid = (l+h)//2
#     if (arr[mid]==0 or arr[mid-1]<=arr[mid]) and (arr[mid] == n-1 or arr[mid]>=arr[mid+1]):
#         return mid
#     else:
#         if mid>0 and arr[mid-1]>arr[mid]:
#             return recursive_method(arr,n,l,mid-1)
#         else:
#             return recursive_method(arr,n,mid+1,h)
        

# def peak_recursive(arr,n):

#     return recursive_method(arr,n,0,n-1) 


# arr= [1,2,3,45,5]
# n= len(arr)
# print(peak_recursive(arr,n))

      