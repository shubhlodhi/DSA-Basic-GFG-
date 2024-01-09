def larger_elments(l):
    sum = l[0]
    for i in l:
        if i>sum:
            sum = i
    return sum
l = [1,2,3,4,5,16,7,8,9]
print(larger_elments(l))
