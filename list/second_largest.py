def maxi(l):
 maximum = max(l)
 sec_max  = None
 for i in l:
    if i != maximum:
        if sec_max == None:
            sec_max = i
        else:
            sec_max = max(sec_max,i)
 return sec_max
   
    # if sec_max <i:
l = [12,13,14,15,12,1,1]
print(maxi(l))


def max_second(l):
   maximum = max(l)
   sec_max = None
   for i in l:
      if i != maximum:
         if sec_max == None:
            sec_max = i
         else:
            sec_max = max(sec_max,i)

        

    