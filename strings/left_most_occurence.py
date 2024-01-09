import sys
# def left_most(st,n):
#     # char  = 256
#     count = [0]*256
#     for i in range(0,n):
        
#         count[ord(st[i])]+=1

#     for i in range(0,n):
#         if count[ord(st[i])] >1:
#             return i
    


# st = "abcdbcd"
# n = len(st)
# print(left_most(st,n)) 

# time complexity  O(n)

# effient approach:

def left_most(st,n):
    count  = [-1]*256
    max = sys.maxsize  # it tends to infinite
    for i in range(0,n):
        if count[ord(st[i])] == -1:
            count[ord(st[i])] = i
        else:
            max = min(max,count[ord(st[i])])

    if max == sys.maxsize:
        return -1
    else:
        return max

st = "abcdbcd"
n = len(st)
print(left_most(st,n)) 