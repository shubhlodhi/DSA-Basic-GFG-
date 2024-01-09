# it is an approach where we find the number which are prime and divisible by 100. 
# output looks like:
# input : n=100 
#  output : 2,2,5,5 , there are only two number between in 100 which are satisfy a condition.


def prime(n):
    for i in range(2,n):

        if n%i ==0:
            return False
        
    return True

def prime_factorization(n):
    for i in range(2,n+1):
        if prime(i):
         x = i
         while (n % x) == 0:
            print(i, end=" ")
            x = x*i

print(prime_factorization(100))

