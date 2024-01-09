def kadane(a,n):
   res  =0
#    maxi =0
   for i in range(0,n):
      maxi =0
      for j in range(i,n):
         maxi += a[j]
         res = max(res,maxi)
   return res
a =[1,2,3,-2,5]
n =len(a)
print(kadane(a,n))

def cut(n,a,b,c):
#    res =0
   if n < 0:
      return -1
   if n == 0:
      return 0 
   res = max(cut(n-a , a,b,c),cut(n-b , a,b,c),cut(n-c ,a,b,c))
   if res == -1:
      return -1
   return res+1
a = 23
print(cut(a,11,12,9))