def sum(n ):
    if  n<10:
        return 1
    return 1+sum(n//10)
    # print(sums)

print(sum(99999 ))


def sum2(n,x):
    if n<1:
        return x
    return sum2(n-1 , x)*x


sum2(5,2)