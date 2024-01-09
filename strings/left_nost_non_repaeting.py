import sys
# def non_repeating(st,n):
#     # char = [0]*256
#     for i in range(0,n):
#         flag = False
#         for j in range(i+1,n):
#             if st[i] == st[j]:
#                 flag = True
#                 break
            
#         if flag == False:
#             return i

#     # return -1
    

# a = "abcadcd"
# n = len(a)
# print(non_repeating(a,n))

# time complexity is O(N^2)

# def non_repating(st,n):
#     char = [0]*256
#     for i in range(0,n):
#         char[ord(st[i])] +=1
    
#     for i in range(0,n):

#      if char[ord(st[i])] == 1:
#         return i

# a = "abcadcd"
# n = len(a)
# print(non_repating(a,n))

# time complexity O(n)
cha  = 256
def non_repeting(st,n):
    char = [-1]*256
    for i in range(0,n):
        if char[ord(st[i])] == -1:
            char[ord(st[i])] =i
        else:
            char[ord(st[i])] = -2

    max = sys.maxsize
    for i in range(0,cha):
        if char[i]>=0:
         max = min(max,char[i])
    if max == sys.maxsize:
        return -1
    else:
        return max

a = "abcadcd"
n = len(a)
print(non_repeting(a,n))