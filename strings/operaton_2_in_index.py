s  = "geeksforgeeks hello"
print(s.startswith("geeks"))
print(s.endswith("geeks"))
print(s.startswith("geeks" ,1))
print(s.endswith("hello" ,16))

# split method 
s1 = "h,elo shu,bh lod,hi"
print(s1.split(","))
print(s1.split())
print(s1.split("s"))
# join method is reverse of split

# s2 = "heloo shubh lodhi"
s2 = ["helo" , "shubh" , "lodhi"]

print("".join(s2))
print(" ".join(s2))
print(",".join(s2))
#  strip method
s3 = "---shubh lodhi---"
print(s3.strip("-"))
print(s3.strip(""))
print(s3.lstrip("-"))
print(s3.rstrip("-"))
print(s3.strip(" "))

# find is method is like the index method but it doesnot generate any error if any value isnot find it will come with with the output -1

s4 = "shubh lodhi"
s5 = "shubh"
print(s4.find(s5))
print(s4.find(s5,6))

