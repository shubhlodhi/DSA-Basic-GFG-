def factorial(n):
    # j = 1

    # for i in range(2,n+1):
    #     j = j*i
    # return j
    if n == 1:
        return 1
    fact = n*factorial(n-1)

    return fact

print(factorial(10))