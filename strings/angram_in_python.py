# #  angram is a simple conecpt in a string it says if 2 strings have same length then check the if they are same in value

# def angram(str,str1):
#     if len(str) != len(str1):
#         return False
#     count = [0]*256
#     for i in range(0,len(str)):
#         count[ord(str[i])] +=1
#         count[ord(str1[i])] -=1
#     for i in count:
#         if i!=0:
#             return False
    


#     return True

# s1 = "abcd"
# s2 = "cdab"
# print(angram(s1,s2)) 
#   time complexuty = O(n)


def angra(str,str1):
    if len(str) != len(str1):
        return False
    s = sorted(str)
    s1 = sorted(str1)
    if s == s1:
        return True
    else:
        return False


s1 = "abcd"
s2 = "cdab"
print(angra(s1,s2))

# s = "subh"
s = [2,1,3,4]
# print(sorted(s))
s1 = s.sort()
print(s1)
print(ord(""))
    
