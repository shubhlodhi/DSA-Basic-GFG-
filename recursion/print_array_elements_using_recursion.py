# n=  [1,2,3,4,5]
def print_array(n):
    if n == 0:
        return
    print_array(n-1)
    print(n)

n = [1,2,3,4,5]
print(print_array(n))
