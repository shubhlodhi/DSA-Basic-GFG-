def interscetion(a,b):
    i,j=0,0
    # temp = []
    while i<len(a) and j<len(b):
        if i>0 and a[i] == a[i-1]:
            i+=1 
            continue
        
        if a[i] < b[j]:
                i+=1
            
                    
        elif a[i] > b[j]:

                    j+=1
        else:
                    # a[i] == b[j]:
                    print( a[i] , end=" ")
            # temp.append(a[i])
                    i+=1
                    j+=1
            
        # return temp
a  =  [1,2,3,4]
b  = [2,3,4]

(interscetion(a,b))

                

