def floor(arr,x):
    floor_number = None
    for i in arr:
        if i < x:
          if floor_number is None or i-x>floor_number-x:
             print(i,"i",end="")
             print(floor_number,"FN",end="")
             floor_number = i
    return floor_number 
        #   else:
            #  floor_number = min(floor_number,i)
    # return -1
arr = [1,2,3,5,12,45]
print(floor(arr,4))




    

            


