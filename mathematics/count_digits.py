# n = 1234
# res = 0

# while n>0:
#     n = n//10
#     res +=1
# print( res)    
def count(n):
    res = 0
    while n>0:
        n = n//10
        res +=1
    return res


print(count(12230))