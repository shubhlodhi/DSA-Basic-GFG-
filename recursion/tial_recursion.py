def fun(n , index):
    if index ==len(n):
        
        return 
    print(n[index])
    fun(n , index+1)
n = [1,2,3,4,5]
print(fun(n,0))

    # print(n)
    #  this is  a type of function is a tail recursion.

