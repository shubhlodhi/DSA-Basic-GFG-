def reverse(str):
    # str = input("enter the string")
    rev = ""
    for i in str:
        rev = i+rev
    return rev


print(reverse("shubh"))

#  second method:

s = "shubh"
print(s[0:5:2])
print(s[::-1])
