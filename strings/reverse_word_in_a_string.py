def reverse(st,l,h):
    while l<h:
     st[l] ,st[h] = st[h],st[l]
     l+=1
     h-=1

def main_reverse(st,l,h):
   l=0
   h = len(st)
   for i in range(0,h):
      if st[i] ==" ":
        reverse(st,l,i-1)
        l = h+1
   reverse(st,l,i-1)
   reverse(st,0,h-1)
   
