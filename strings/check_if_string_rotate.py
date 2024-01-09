# s = "abcd"
# s1 = "f"
# s2 = s+s
# if (s2.find(s1)):
#     print("yes")
# else:
#     print("no")

def check(s1,s2):
    if len(s1)!= (len(s2)):
        return False
    temp = ""
    temp = s1+s1
    return temp.find(s2)!=-1

s1 = "abcd"
s2 = "cdab"
print(check(s1,s2))
