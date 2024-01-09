# def divisor(n):
#     for i in range(1,n+1):
#         if n%i == 0:
#             print(i)

# print(divisor(15))


#  here to reduce the time complexity of n we use the pair , divisor always appear in pair , heer are some example: (1,30) , (2,15) , (3,10) , (5,6)
# so here x+y = n . so x is smaller than n , so x*x >= root of n.

def divisor(n):
    i =1
    while i*i<=n:
        if n%i ==0:
            print(i)

        # i+=1
        #     if i != n/i:
        #         # print(i)
        #         # print(n)
        #         print(n//i)
        i+=1

    while i>=1:
        if n%i==0:
            print(n//i)
        i-=1

print(divisor(15))

