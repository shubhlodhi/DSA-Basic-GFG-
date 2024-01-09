def first_occurence(l,k):
    for i in range(len(l)):
        if l[i] == k:
            return i
def last_occurence(l,k):
    for i in range(len(l)-1 ,0,-1):
        if l[i] == k:
            return i
def count(l,k):
    first = first_occurence(l,k)
    if first == -1:
        return 0
    else:
        return last_occurence(l,k) - first+1

l = [0,0,0,1,1,1,1,1]
# print(last_occurence(l,1))
# print(first_occurence(l,1))
print(count(l,1))

