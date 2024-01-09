#  absolut value:
# input:-5 ,output:5
def absolute(n):
    res = 0
    for i in range(-1,n-1,-1):
        res+=1
        # print(i)
    return res


print(absolute(-9))

# how to convert farenheit to celcius
# (32°F − 32) × 5/9 = 0°C
def convert_F_C(F_value):
    return (F_value-32) * 5/9
print(convert_F_C(67))

def factorial_number(n):
    if n == 0:
        return 1
    else:
        fact = n*(factorial_number(n-1))
        return fact
print(factorial_number(5))
def fact_iterative(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res 
print(fact_iterative(5))
def count_digit_in_face(n):
    fact = factorial_number(n)
    res=0
    while fact>0:
        res +=1
        fact = fact//10
    return res

print(count_digit_in_face(5))

def check_if_number_is_prime(n):
    if n%2 ==0 or n%3==0:
        return False
    else:
        return True

print(check_if_number_is_prime(7))
def isprime(n):
        factor = 2
        # res =0
        while(factor*factor)<=n:
            if n%factor==0:
                # print(factor,n)
                return False
            factor+=1
        return True

def xactly_3_divisor(n):
    
    p = 2
    ans = 0
    while(p*p)<=n:
        if isprime(p)==True:
            print("p" ,p)
            ans+=1
        p+=1
    return ans

print(xactly_3_divisor(6))

# If D > 0:
#         => This occurs when b2 > 4ac.
#         => The roots are real and unequal.
#         => The roots are {-b + ?(b2 – 4ac)}/2a and {-b – ?(b2 – 4ac)}/2a.

# If D = 0:
#         => This occurs when b2 = 4ac.
#         => The roots are real and equal.
#         => The roots are (-b/2a).

# If D < 0:
#         => This occurs when b2 < 4ac.
#         => The roots are imaginary and unequal.
#         => The discriminant can be written as (-1 * -D).
#         => As D is negative, -D will be positive.
#         => The roots are {-b ± ?(-1*-D)} / 2a = {-b ± i?(-D)} / 2a = {-b ± i?-(b2 – 4ac)}/2a where i = ?-1.

# Use the following pseudo algorithm to find the roots of the 

# Pseudo algorithm:

# Start
# Read the values of a, b, c
# Compute d = b2 – 4ac
# If d > 0
#     calculate root1 = {-b + ?(b2 – 4ac)}/2a
#     calculate root2 = {-b – ?(b2 – 4ac)}/2a
# else If d = 0
#     calculate root1 = root2 = (-b/2a)
# else
#     calculate root1 = {-b + i?-(b2 – 4ac)}/2a
    # calculate root2 = {-b + i?-(b2 – 4ac)}/2a
# print root1 and root2

    
