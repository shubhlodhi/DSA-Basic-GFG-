# print(12%6)
# naive approach

def lcm(a,b):
    maximum = max(a,b)
    while a != b:
        if maximum%a==0 and maximum%b==0:
            return  maximum
        maximum+=1
    return maximum

print(lcm(4,6))


# effective approach

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)
a = 4
b = 6
print(lcm(a,b))

