# def base(n):
#     if n == 0:
#         return
#     # print(n)
#     base(n-1) 
#     print(n)
#     base(n-1)
    # first it executes the base condition 


# (base(3))

# def fun(n):
    # if n<=1:
        # return 0
    
    
    # 1+fun(n//2)
    # print(n)


# fun(16)


# def fun2(n):
    # if n == 0:
        # return 
    # fun2(n//10)
    # print(n%2)
    # print(n)

# fun2(245)

def sum(n):
    if n < 10:
        return n
    return sum(n//10)+n%10

print(sum(245))



# print(245%10)
def one_to_n(n):
    if n == 0:
        return 
    # one_to_n(n-1)
    print(n)
    one_to_n(n-1)

print(one_to_n(3))