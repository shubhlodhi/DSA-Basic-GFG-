def fun(n):
    sum = 0
    for i in range(1,n+1):
        print("i",i ,end="")
        for j in range(1,i+1):
            print("j" ,j,end="")
            sum =+1
    return(sum)



print(fun(3))