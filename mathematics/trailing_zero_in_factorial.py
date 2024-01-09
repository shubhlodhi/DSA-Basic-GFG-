#  it is  a naive approach .
# def factorial(n):


#     j = 1
#     for i in range(2,n+1):
#         j = j*i
#     return j
    
#     # if n == 1:
#         # return 1 
#     # fact = n*factorial(n-1)
#     # res = 0
#     # while(j%10==0):
#     #     res +=1
#     #     j = j//10
#     # return res

# print(factorial(10))

# effcient approach:
def trailing_zero(n):
    res = 0
    i = 5
    while i<=n:
        res = res + n//i
        i = i*5
    return res

print(trailing_zero(251))