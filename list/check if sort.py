def is_sort(l):
    n = len(l)
    sorted = True
    # i = 0
    for i in range(0,n-1):
        if l[i] > l[i+1]:
            # i+=1
          sorted = False
        # else:
    return sorted
l = [1,2,3,4,5,6]
print(is_sort(l))