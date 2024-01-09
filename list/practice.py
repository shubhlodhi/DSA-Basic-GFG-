# def get_elements(arr,index,elements):
#     for i in range(index):
#         if i == elements:
#             return arr[i]
#     return -1
# a =[1,23,3,4]
# n =len(a)
# print(get_elements(a,n,1))

def get_immediate_greater(arr,n,x):
    a = []
    for i in range(n):
        if arr[i] > x:
            a.append(arr[i])
    if len(a) == 0:
        return -1
    else: 
        
        maxi = min(a)
    a.sort()
    # return 
    return maxi
   
a = [63,6,60,38,3,94,43,83,65]
# 63 6 60 38 3 94 43 83 65
# 18
n =len(a)
print(get_immediate_greater(a,n,18))

# def compare_two_elemnget_elements(arr,n,x,y):
#     res =0
#     res1= 0
#     for i in range(n):
        
#         if arr[i] == x:
#             res+=1
#     for j in range(n):
        
#         if arr[j]==y:
#             res1+=1
#     print(res)
#     print(res1)
#     if res == res1:
#         return res
#     elif res > res1:
    
#         return x
#     else:
#         return y
    
# a = [1,2,3,3,3,3,4,4,4]
# n =len(a)
# print(compare_two_elemnget_elements(a,n,3,4))


def rotate(arr,n,r):

    last_element = arr[0]
    i =1
    for j in range(r):
     while i<n:
        arr[i-1] = arr[i]
        i+=1

    arr[n-1] = last_element
    # return arr
a = [1,2,3,4]
n = len(a)

print(rotate(a,n,2))
print(a)

# def rotateArr(A,D,N):
#         #Your code here
#         D = 2
#         last_elements = A[0]
#         while D>0:
#             for i in range(1,N):
#                 A[i-1] = A[i]
#             A[N-1] = last_elements
            
#             D+=1
#         return A
# a  =[1,2,3,4]
# n = len(a)
# print(rotateArr(a,2,n))


def print1ton(arr,n):
    if n == 0:
        return 1
    # print(arr[n])
    print1ton(arr,n-1)
    print(arr[n] , end=" ")
a = [1,2,3,4]
n= len(a)
(print1ton(a,n))
        

        

