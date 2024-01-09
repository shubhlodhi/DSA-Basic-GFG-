# def immeduate(arr , n,x):
#     maximum = max(arr)
#     maxi  = x

#     immediate_max = None
#     for i in range(x):
#         if i != maxi:
#          if immediate_max == None:
#             immediate_max  = i
#         else:
#             immediate_max  = max(immediate_max,i)
#     return immediate_max

# arr = [1,2,3,4,5]

# n = len(arr)
# print(immeduate(arr,n,4))
# # print(arr)
# def add(addl):
#    addl += [10]
#    return addl


# s = [10,20,30,40]
# print(add(s))

# In this problem, you need to find the number of elements in the array that are smaller than X and also find the element that is the closest to X with the minimum difference. You can modify the previous code to achieve this:

# python
# Copy code
def find_immediate_greater_than_x(arr, X):
    immediate_greater = None  # Initialize as None to handle cases where there is no greater element
    
    for num in arr:
        if num < X:
            if immediate_greater is None or num - X > immediate_greater - X:
                immediate_greater = num
            # print(immediate_greater)
    
    return immediate_greater

# Example usage:
arr = [4, 67, 13,17, 12, 15]
X = 16
result = find_immediate_greater_than_x(arr, X)
print(result)
# list = [2001,2002]
# list1 = [2003,2006]
# print((list+list1)*2)

