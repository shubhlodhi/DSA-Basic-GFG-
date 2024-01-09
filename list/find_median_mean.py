def median(arr ,n):
    s = arr.sort()
    # for i in range(n):
    if n%2==0:
        mid1 = s[n//2-1] 
        mid2 = s[n//2]
        return (mid1+mid2)//2
    else:
        return s[n//2]
def mean(arr ,n):
    return sum(arr) // n



