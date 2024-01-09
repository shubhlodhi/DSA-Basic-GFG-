
# l = [1,2,3,4,6,5]
# g = 4
# s = [x for x in l if g<x]
# print(s)


def find_greater_than_x(arr ,n):
    for i in arr:
        if i>n:
            print(i," ")

l = [1,2,3,4]

find_greater_than_x(l , 2)