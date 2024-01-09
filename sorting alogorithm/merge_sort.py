def merge_sort(l):
    divide = (l//2)
    left = l[:divide]
    right = l[divide:]
    merge_sort(left)
    merge_sort(right)
    return sorted(left,right)


def sorted(right,left):
    i =j =0
    merged =[]
    while i<len(right)  and j<len(left):
        if right[i] > left[j]:
            merged.append(left[j])
            i+=1
        else:
            merged.append(right[i])
            j+=1

        while i<len(right):
            merged.append(right[i])
            i+=1
        while j<len(left):
            merged.append(left(j))
            j+=1

    return merged
 
a = [1,4,6]
b = [5,8,2]
n = len(a)
print(sorted(a,b))
