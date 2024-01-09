def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1],arr[j]

    return arr

a = [13,2,4,6,5]
n = len(a)
print(bubble_sort(a,n))

def insertion(arr,n):
    for i in range(1,n):
     x = arr[i]
     j = i-1
     while j>=0 and arr[j] > x:
        arr[j+1] = arr[j]
        j = j-1
     arr[j+1] = x
    return arr
a = [13,2,4,6,5]
# a = [2,13,4,6,5]
# a = [2,4,13,6,5]
n = len(a)
print(insertion(a,n))

def quick_sprt(arr,n,):
   arr1 =[]
   low = 0
   high = n-1
   mid = (low+high)//2
   arr2 = arr[:mid]
   i =0

   arr3 = arr[mid:]
   j=0
   while i<len(arr2) and j<len(arr3):
      if arr2[i]> arr3[j]:
         arr1.append(arr3[j])
         j+=1

      else:
         arr1.append(arr2[i])
         i+=1

   while i<len(arr2):
      arr1.append(arr2[i])
      i+=1
   while j<len(arr3):
      arr1.append(arr3[j])
      j+=1

#    print(arr2)
#    print(arr3)
   return arr1
a = [2,4,13,6,5]
n = len(a)
print(quick_sprt(a,n))

def count_invrersion(arr,n):
   res =0
   for i in range((n)):
      for j in range(1,(n)-i):
         if arr[i]>arr[j]:
            res +=1
   return res  

a = [2,4,13,6,5]
n = len(a)
print(count_invrersion(a,n))




    
      

   
      
      
