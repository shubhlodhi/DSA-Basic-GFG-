# coprension find odd or even
n = [1,2,3,5]


s = [x for x in range(11) if x%2==0]
print(s)
o = [x for x in range(11) if x%2!=0]

print(o)
# d = [x for x in n if x%n==0]
# print(d)

# comprhension find the smallest numbers from x 

def find_smaller(l,x):
    return [e for e in l if e<x]

l = [3,15,12,9,7]
x = 10

print(find_smaller(l,x))

# find odd even in list:

def odd_even(l):
    odd = [x for x in l if x%2==0 ]
    even = [x for x in l if x%2!=0]
    return odd, even
l = [1,2,3,4,5,6,7,8,9]
evensss,odds =(odd_even(l))
print(evensss)
print(odds)

# using comphrension in string:


l = "geeks for geeks"
d = [x for x in l if x in "aeiou" ]
print(d)

for i in l:
    if i in "aeiou":
        print(i , end=" ")


l2 = ["geeks" , "gfg" , "Hello"]
# for i in l2:
    # if i.startswith("g"):
        # print(i)
l3 = [x for x in l2 if x.startswith("g")]
print(l3)


ww = [x*2 for x in range(6)]
print(ww)

ww1 = [x.upper() for x in l2 if x.startswith("g")]
print(ww1)


# dictionary using comphrension:


dic = {x:f"id:{x**2}" for x in range(6)}



print(dic)


# inverse the dictinary
d = {"122" : "shubh" , "22" : "Lodhi"}
dic1 = {k:v for v,k in l}
print(dic1)