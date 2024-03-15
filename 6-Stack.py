
#           ===================================             Stack                   ================================

""" 

1 - Intro to stack
2 - Functions associated with stack  -  (push , pop , top etc.)
3 - Implementation of stack    - ( list , collection , queues)
"""

#           ===================================             Stack                   ================================

""" 
1 - It follows LIFO
2 - Insertion and removal as done at  one end 
3 - PUSH is used to insert an element in a stack
4 - POP is used to Removal an element in a stack


"""

#           ===================================             Functions in stack                   ================================

"""
1 - push(x)  -  used to insert the element x at the end
2 - pop()    -  used to remove the top element/last element of the stack     
3 - size()   -  gives the length of the stack
4 - top()    -  give reference of the last/top element present in the stack
5 - empty()  -  returns True for an empty stack


note :- The time complexity of every function above is               O(1)
   
"""


#           ===================================             Implementation of stack                   ================================

""" 
1 - List  --> List in python can be used as a stack

              append()  --> It is used to insert the element                    ( because time complexity is O(n) )
              pop()     --> It is used to remove the last element
 
Syntax :

   stack = []
   stack.append("abc")
   print(stack.pop()) 


"""

stack = []

stack.append("welcome")
stack.append("To")
stack.append("Codeing")

print(stack)

stack.pop()

print(stack)

#           ===================================             Implementation of Deque                   ================================

"""

 1- Stacks in python are created by collection module which deque class 
 2- append and pop functions are faster in deque as compared to list      ( because time complexity is O(1) )
 

"""

from collections import deque

st1 = deque()

st1.append("abc")

print(st1)

st1.append("abc")
st1.append("red")
st1.append("blue")
st1.append("Green")

print(st1)

st1.pop()

print(st1)


#           ===================================             Implementation of Queue                   ================================


