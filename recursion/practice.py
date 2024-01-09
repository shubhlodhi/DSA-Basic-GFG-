# def one_to_n(n):
#     if n == 0:
#         return
#     print(n)
    # one_to_n(n-1)
    


# one_to_n(3)

# def print_elements(n , index):
#     if index >= len(n):
#         return 
#     print(n[index])
#     print_elements(n,index+1)
# n = [1,2,3,4,5]
# print(print_elements(n , 0))


# def sum_of_a_digit(n):
#     if n<10:
#         return n
#     return sum_of_a_digit(n//10)+n%10


# print(sum_of_a_digit(256))

# def count_digit_in_a_number(n):
#     if n<10:
#         return 1
#     return count_digit_in_a_number (n//10)+1

# print(count_digit_in_a_number(123))

# def print_elemnts(arr,n):
#     if n==len(arr):
#         return 
#     print(arr[n] , end=" ")
#     print_elemnts(arr,n+1)
# na = [1,2,3,4,5]
# print(print_elemnts(na , 0))

# def sum(n):
#     if n<10:
#         return 1
#     return sum(n//10)+1


# print(sum(999990))
    
def fibnaci(n):
    if n <= 1:
         return n
    return (fibnaci(n-1)+ fibnaci(n-2))

print(fibnaci(20))
# print(999%10)
# def power(n,r):
#      if n==1:return
#      return power(n-1,r)+(n+1)
# print(power(5,2))
# # print(99%10)
# print(9%10)

# def gcd(n,m,low):
#      if low>=n:
#           return 0
#      low//n==0 and low//m==0
#      gcd(n,m,low+1)
#      return low 


#     #  else:
#         #   return -1
     
# print(gcd(2,4,1))

# print(2//4)
def hcfnaive(a, b):
    if(b == 0):
        return (a)
    else:
        return hcfnaive(b, a % b)
print(hcfnaive(7,8))


def recursiveSum(n):
        if n ==0:
            return 0
        else:
            
            return recursiveSum(n-1)+(n)
# print(recursiveSum(5))
class Solution:
    def isPalin(self,N):
        N = str(N)
        def ispalind(N):
         low = 0
         high = N-1
        #code here
        
         
         if len(N)<=1:
            return 0
        # low = 0
        # high/ = N-1
        # if low>=high:
            # return True
         if N[0] == N[-1]:
          self.ispalind(self,N[1:-1])
         return 1
        
s = Solution()
s.isPalin(111)

def sum(n):
    if n ==0:
        return n
    else:
        return sum(n//10)+n%10
print(sum(555))

def factorial(n):
    if n ==0:
        return 1
    return factorial(n-1)*n
print(factorial(4))
