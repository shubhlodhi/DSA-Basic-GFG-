
import math


def find(arr,n):
    count = 0
    for i in range (0,n):
        if arr[i]%2==0 or arr[i]%2!=1:
            count+=1
            for j in range(1,n):
             if arr[i]%2 == 0 and arr[j]%2!=0:
                count+=1
             if arr[i]%2!=0 and arr[j]%2==0:
                count+=1
             else:
                break
             return count        
        
a = [10,12,14,7,8]
n = len(a)
print(find(a,n))

def find2(arr,n):
   count = 1
   for i in range(1,n):
      if arr[i]%2==0:
         if arr[i-1]%2!=0:
            count+=1
      if arr[i]%2!=0:
         if arr[i-1]%2==0:
            count+=1
   return count

a = [7,8,13,14]
n = len(a)
print(find2(a,n))

def maojority(arr,n):
   majority = (n+1)//2
   res=0
   for i in range(0,n):
      count =0
      for j in range(0,n):
         if arr[i] == arr[j]:
            count+=1
         if count > majority:
             res = max(res,count)
             return arr[i]
         else:
            break
#    return i
arr = [3,7,4,7]
n = len(arr)
print(maojority(arr,n))
         
def majo(arr,n):
   maxi =0
   majoir = (n)//2

   for i in range(0,n):
      count =0
      for j in range(0,n):
         if arr[i] == arr[j]:
            count+=1
            maxi = max(maxi,count)
      if maxi > majoir:
         return i
   return 0
      
arr = [20,40,50,50,50]
n = len(arr)
print(majo(arr,n))

def flip(arr,n):
   count=0
   for i in range(0,n):
      for j in range(i+1,n):
         if arr[i] ==  arr[j]:
            count+=1
         if arr[i] != arr[j]:
            index = (f" from {i} to {j-1}")
            # return i
            break

a = [1,1,0,0,0,1]
n = len(a)
flip(a,n)
def flop2(a,n):
   for i in range(0,n):
      if a[i] == 0:
         index = i
         break

   for j in range(index,n):
      if a[j] != 0:
         index1 = j-1
         break

   print(f"from {index} to {index1}")
a = [1,1,0,0,0,1]
n = len(a)
flop2(a,n)
def flip1(a,n):
   for i in range(0,n):
      for j in range(i+1,n):
         if a[i]==a[j]:
            index = j

         # print(f"from{i} to {j}")

         if a[i]!=a[j]:
            if a[i]==a[j-1]:
             print(f"from{i} to {j-1}")
            break


a = [1,1,0,0,0,1]
n = len(a)
flip1(a,n)
def sliding(a,n,k):
   maxi =0
   # i  =0
   for i in range(0,n+1-k):
   # while (i+k-1<n):

      curr = 0
      for j in range(k):
         curr += a[i+j]
      maxi = max(maxi,curr)
      # i+=1
   return maxi
a = [10,5,-2,20,1]
n = len(a)
print(sliding(a,n,3))

def sum(a,n,sumi):
   for i in range(0,n):
      curr =0
      for j in range(i,n):
         curr += a[j]
         if curr == sumi:
            return "yes"
   return 0
a1 = [1,4,20,3,10,5]
n = len(a1)

print(sum(a1,n,24))

def sum1(arr,n,sum):
   curr = 0
   for i in range(0,n):
      curr+=arr[i]
      if curr == sum:
         return 1
      if curr>sum:
         
         # i=0
         # curr -= arr[i]
         # i+=1
         # curr =0
         break
   for j in range(0,i+1):
      # print(i)
      if curr>sum:
       curr -= arr[j]
   if curr == sum:
         return 1
   return 0

# a1 = [1,4,20,3,10,5]
a1 = [4,8,12,5]
n = len(a1)
print(sum1(a1,n,17))

   # curr =0
   # for i in range(i+1,n):
   #    # if curr  > sum:
   #    # curr = 0

   #    curr += arr[i]

def  ppemd(arr,l,h):
   curr = 0
   a1 = []
   i =0
   while i<len(arr):
      curr = curr+arr[i]
      a1.append(curr)
      i+=1
   print(a1)
   print(a1[h]-a1[l-1])

a = [2,8,3,9,6,5,4]
print(ppemd(a,2,3))

def equilib(ar,n):
   
   for i in range(n):
      l ,h =0,0
      for j in range(i):
         l += ar[j]
      for k in range(i+1,n):
         h += ar[k]

      if l == h:
         return ar[i]
   return 0

a = [3,4,8,-9,20,6]
n = len(a)
print(equilib(a,n))

# def eq(a):
#    sumi = sum(a)
#    ls = 0
#    for i in range(len(a)):
#       sumi = sumi-a[i]
#       if sumi == ls:
#          return True
#       ls+=a[i]

#    return 0

# a = [3,4,8,-9,20,6]
# # n = len(a)
# print(eq(a))

def macimumm(a,b):
   sl  = [0]*100
   # i =0
   for i in range(len(a)):
    for j in range(a[i] , b[i]+1):
      sl[j]+=1

   maxc = sl.index(max(sl))
   return maxc

a = [1,2,5,15]
b = [5,8,7,18]
print(macimumm(a,b))

def rorttae(a,n):
   count =0
   for i in range(0,n-1):
      if a[i] != i+1:
         count+=1
         for i in range(1,n):
            a[i-1] = a[i] 
         a[n-1] = a[0]
   return count


a = [2,3,1]
n = len(a)
print(rorttae(a,n))


def rro(a,n):
   maxi = max(a)
   mini = min(a)
   count =0
   if a.index(maxi) == a.index(mini)-1:
      # count =0
      print(" it is increasing order")
      if a[n-1] < a[0]:
         print("yes")
      # for i in range(maxi,n+1):
         # count+=1
      # print(count)
   if a.index(maxi)-1 == a.index(mini):
      print("it is in decraesing order")
      if a[n-1]>a[0]:
         print("yes")
      # for i in range(mini,n+1):
         # count+=1
      # print(count)

   return -1

a = [3,4,5,1,2]
n = len(a)
rro(a,n)
   



# a = [2,3,1]
# n = len(a)
# print(rro(a,n))
# maxi = a.index(max(a))
# print(maxi)



def reaarange(a,n):
   a1 =[]
   for i in range(0,n):
      w = a[i]
      a[i] = (a[a[i]])
      a[i] = w

   return a

a =[4,0,2,1,3]
n= len(a)
print(reaarange(a,n))
print(8//5)
print(1 + math.sqrt(5))


def misisng(ar,n):
   fond = True
   for i in range(1,n+1):
      if ar[i-1] == i:
         print(i , end="")
         print(ar[i-1])
      else:
         fond = False
         return i
      
a = [2,3,1,4,5]
n = len(a)
print(misisng(a,n))

def stb(a,n,l,h):
   # l =0
   if l>=h:
      return 0
   # h =n-1
   res =0

   for i in range(l,h):
      for j in range(i+1,n):
         if a[j]>a[i]:
            curr = a[j]-a[i] + stb(a,n,l,i-1)+ stb(a,n,j+1,h)
            res = max(res , curr)
   return res

a =[100,180,260,310,40,535,698]
n =len(a)
print(stb(a,n,-0,n-1))


# def strpin(a,n):
#    res= 0
#    for i in range(0,n):
#       for j in range(1,n-1):
#          count =  arr[i]-arr[j]
#          res = max(res,count)
#    return res
# a =[3,0,0,2,0,4]
# n =len(a)
# print(strpin(a,n))
         
# def code(a,n):
#    maxi = max(a)
#    mini = min(a)
#    i =0
#    y =0
#    for j in range(n-1):
#       if arr[i] < arr[i+1]:
#          x+=1
#       else:
#          y+=1
#    if y==1:
#       if arr[0]>arr[n-1]:
#          i+=1
#       else:
#          y+=1
#       if y==1:
#          return True
#    return False
   # if a.index(maxi) == a.index(mini)-1:
   #    if a[0]>a[n-1]:
   #       return "Yes"
   # if a.index(mini) == a.index(maxi)-1:
   #    if a[0]<a[n-1]:
   #       return "yes"
   # return "No"
# a = [1,2,3]
# n = len(a)
# print(code(a,n))

def index(a,n):
   res =0
   for i in range(0,n):
      count  =0
      for j in range(i+1,n):
         if a[j]>a[i]:
            count = j-i
            res = max(count,res)
   return res

a = [34,8,10,3,2,80,30,33,1]
n =len(a)
print(index(a,n))