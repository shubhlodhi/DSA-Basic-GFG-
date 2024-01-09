def insert(arr,n,index,elemnts):
    if index>0 and index<n:
        return arr.insert(index,elemnts)
    else:
        return "error list"


l = [1,2,3,4]
n = len(l)
(insert(l,n,1,78))
print(l)
