#           ===================================             Array                 ================================

""" 
 1 -  Linear Data Structure
 2 -  Contiguous memory location 
 3 -  Access Elements Randomly
 4 -  Homogeneous elements ( Similar elements :- cannot store int  string and float in a single array) 
  


"""


""" 
Applications of Array

1 - Storing Information - Linear Fasion
2 - Suaitable for application that require frequent searching


"""

#           ===================================             1-D Array                 ================================

"""

1 - 1D  can be related to a row
2 - Elements are stored one after another
3 - Only one scripted or index is used


"""

# Declaration and Initialization 

""" 
1 - Array Declaration    :-  Datatype varname[size];
2 - Array Initialization :-  Datatype varname[] = { ele1, ele2, ele3, ele4 };                    (ele = element)

"""

#           ===================================             2-D Array                 ================================

"""

1 - 2D  can be related to a Table or Matrix                                                           0               1              2
2 - Elements are stored one after another i.e 1D array inside other                         2d = { {1, 2, 3, 4} , {4, 5, 6, 7} ,  {8, 9, 1, 0} },
3 - Two  subscripts or indices are used, one row and one column,                      indexing     00,01,02,03     10,11,12,13     20,21,22,23
4 - Dimentions depends upon the number of subscripts used


"""

#           ===================================             Array Implimentation                 ================================



#            ======   PQ-1     ========


print(" How many element to store inside the array" , end="")
num= input()

arr = []

print("\nEnter", num, "Element: ", end="")

num= int(num)

for i in range (num):
    element = input()
    arr.append(element)
    
print("\n The array element are")

for i in range(num):
    print(arr[i],end="")
    
    

#            ======   PQ-2     ========

r_num = int(input("input number of rows : "))
c_num = int(input("input number of Columns : "))

twod_arr = [[0 for col in range(c_num)] for row in range (r_num)]

for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col] = row*col
        
print(twod_arr)


#            ======   PQ-3     ========


print(end="Enter the size of the array")
tot = int(input())

arr = []

print(end="Enter" + str(tot) + "Elements :")

for i in range (tot):
    arr.append(input())

print(end= "\n Enter the value to Delete : ")

val = input()

if val in arr:
    arr.remove(val)
    print("\n The new Array is :")
    for i in range (tot-1):
        print(end=arr[i] + "")
    else:
        print("\n Element does not exist in the list")
