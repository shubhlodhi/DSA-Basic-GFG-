# palindrome number is a type of number when it check in a reverese position then it is same as original value:


def palindrome(n):
    res = 0
    temp= n
    while temp != 0:
        check = temp%10
        res = res*10 + check
        temp = temp//10
    if n==res:
        return "yes"
    else:
        return "no"

print(palindrome(72123))