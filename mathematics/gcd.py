# self approach:
#  def self(a,b):

#     maxi = max(a,b)
#     # print(maxi)
#     i= 1
#     while i<maxi:
#         if (i/a==0)and (i/b==0):
#             return i
#         i+=1
#         return False
    
# print(self(12,15))

# naive approach:

# def gcd(a,b):
#     minimum  = min(a,b)
#     maximum = max(a,b)

#     # i = minimum
#     for i in range(1,maximum):
#         if b%minimum==0 and a%minimum==0:
#             return minimum
#         else:
#             minimum -= 1

# a =100
# b = 200
# print(gcd(a,b))

        

# print(15%5)

# def effective_gcd(a,b):
#     while a != b:
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#     return a


def recursive(a,b):
    if b==0:
        return a
    return recursive(b,a%b)


a =4
b = 6
print(recursive(a,b))
print(4%6)


