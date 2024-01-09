def duplicates(arr , n):
    temp = [0]*n
    temp[0] = arr[0]
    res = 1
    for i in range(1,n):
        if temp[res-1] != arr[i]:
            # print(temp[res-1])
            temp[res] = arr[i]
            # print("temp" , temp[res] , end=" ")
            res+=1
    for i in range(0,res):
        # arr[i] = temp[i]
      return temp
    
# def duplicates (arr , n):
#     for i in range(n):
#         x = arr[i]%n
#         arr[x] = arr[x]+n 

#     for i in range(0,n):
#         if arr[i]>n*2:
#             print(i , end="")      

l = [1,1,2,2,3,3,3,4,4,4,4 ,10,10,10]
n = len(l)
print(duplicates(l ,n ))

