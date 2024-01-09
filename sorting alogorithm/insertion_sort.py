def insertion_sort(arr,n):

    for i in range(1,n):
            x =arr[i]
            j = i-1
            while j>=0 and x<arr[j]:
             arr[j+1] = arr[j]
             j = j-1
             arr[j+1] = x
    return arr


a = [1,3,2,4,5 , 10,5]
n =len(a)
print(insertion_sort(a ,n))

