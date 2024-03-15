tup1 = (1, "a", True, "b", 33.2)
el1 = tup1[2:5]

print(el1)

  
#           ===================================             LIST                 ================================
lis1 = [11, "va", True, "b", 33.2]
el2 = lis1[1:4]

print(el2)


#           ===================================             Dict                 ================================
dic1 = {
    "Mango" : 10,
    "orange" : 20,
    "apple"  : 32,
    "banana" : 60
}

print(dic1.keys())
print(dic1.values())

dic1["Mango"] = 100 

print(dic1)

#           ===================================             SET                  ================================

s1 = {1,1,1,2,2,3,5,69,7,8,9,"d"}

print(s1)

s1.add("hello world")

print(s1)

s1.update(["reddy", 2,55,66,77])

print(s1)
