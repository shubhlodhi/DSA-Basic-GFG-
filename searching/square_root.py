def square_root(n):
    i=1
    while i*i<=n:
        i+=1
    return i-1 

print(square_root(4))


# efficient_method: use binary serach

def square_root(n):
    low = 0
    high = n
    ans =0
    while low<=high:
        mid = (low+high)//2
        maximum = mid*mid
        if maximum == n:
            return mid
        
        elif maximum >n:
                high = mid-1
        else:
                low = mid+1
                ans = mid
    return ans

print(square_root(4))



