# def prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
        
#     return True
    
# def sieve(n):
#     for i in range(1,n+1):
#         if prime(i):
#               print(i)

# print(sieve(15))
        
# def sieve(n):
#     if n<1:
#         return 1
#     isprime  = [True] * (n+1)
#     i = 2
#     while i*i<n:
#         if isprime[i]:
#             for j in range(2*i , n+1,i):
#                 isprime[j] = False
#         i+=1

#     for i in range(2,n+1):
#           if isprime[i]:

#               print(i)        

def sieve(n):
    if n<1:
        return 1
    isprime = [True] * (n+1)
    i = 2
    while i<n:
        if isprime[i]:
            print(i)
            for j in range(i*i , n+1 , i):
                isprime[j] = False
        i+=1
