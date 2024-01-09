#  naive approach:
# def find_prime(n):
#     # i = 2
#     # if n == 1:
#         # return False
#     # while i<n:
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#         # else:
#             # i+=1
#         # i+=1

#     return True
    

# print(find_prime(3))

# print(21%2)

# time complexity = O(n):

#  efficient approach: O(logn)
# def prime(n):
#     i =2
#     while (i*i <= n):
#         if n%i == 0:
#             return False
#         i+=1
#     return True

# print(prime(4))


# more efficeint method:
# step-1 :  in this method we define some value like: if n = 2 or 1 then it is prime or any value which have 0 remainder  or like if is
# step-2 : is divide by 2 and 3 and remainder result is 0 then it is not comes in prime category  
# step-3 : we run a while loop this loop have condition if i*i is smaller then n: then check the condition or else define the n as prime number
# here we define the i as 5 and increement the i value as 6 every time and in while we check a if condition it says if n %i is 0 then it is false  
# else increment to 6


def prime(n):
    if n == 1:
        return True
    if n == 2 or n == 3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while (i*i <= n):
        if n%i ==0 or n%(i+2)==0:
            return False
        i+=6
    return True

print(prime(101))

