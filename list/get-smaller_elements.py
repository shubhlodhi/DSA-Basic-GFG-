def get_smaller(l ,n):
    for i in l:
        if i<=n:
            print(i , end=" ")

l = [1,5,12,13,141,515,13,13,16]
n = 10
print(get_smaller(l,n))

