def sum_N(n):
    if n <0:
        return 0
    return sum_N(n-1)+n


print(sum_N(5))