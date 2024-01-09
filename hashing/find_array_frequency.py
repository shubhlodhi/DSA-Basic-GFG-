# # naive appraoch and its time complexity is O(n^2)

# def freq_of_elements(arr ,n):
#     for i in range(n):
#         flag = False
#         for j in range(i):
#             if arr[i] == arr[j]:
#                 flag = True
#                 break
#         if flag == True:
#             continue
#         res = 1
#         for j in range(i+1,n):
#             if arr[i] == arr[j]:
#                 res +=1

#         print(arr[i] , res)
#         # return res


# a = [10,10,20,20,30]
# n = len(a)
# print(freq_of_elements(a,n))


# efficient approach:  O(n)
def ferq_elemnts(arr,n):
    new_dict = dict()
    for i in range(n):
        if arr[i] in new_dict.keys():
            new_dict[arr[i]] +=1
        else:
            new_dict[arr[i]] = 1
    for x in new_dict:
        print(new_dict[x])
a = [10,10,20,20,30]
n = len(a)
print(ferq_elemnts(a,n))




