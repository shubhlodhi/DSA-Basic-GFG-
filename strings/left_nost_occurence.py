def string(s1,x ,n):
    for i in range(n):
        for j in range(i+1,n):
            if s1[i] == s1[j]:
                return i


s = "abcdbcd"
n = len(s)
print(string(s,"a",n))
# tie complexity is O(n^2)


def effficcient_string(s1,n):
    count = [0]*256
    for i in range(0,n):
        count[ord(s1[i])] +=1

    for i in range(0,n):
        if count[ord(s1[i])] >1:
            return i
    return -1
a = "abcdbdc"
n = len(a)
print(effficcient_string(a,n))
#  time complexity O(N)
