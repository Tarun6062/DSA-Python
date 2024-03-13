


"""  

     ============================================================================== DSA IN PYTHON ================================================================================== 
     
     
Binary Search and Complexity Analysis

Arrays, Stacks, Queues and Strings 

Python Classes and Linked Lists

Binary Search Trees and Hash Tables

Insertion Sort, Merge Sort and Divide-and-Conquer 

Quicksort, Partitions and Average-case Complexity

Recursion, Backtracking and Dynamic Programming 

Knapsack, Subsequence and Matrix Problems 

Graphs, Breadth-First Search and Depth-First Search 

Shortest Paths, Spanning Trees & Topological Sorting

Disjoint Sets and the Union Find Algorithm 

Interview Questions, Tips & Practical Advice 
     

"""


#    =============================  HOW TO SOLVE PROBLEMS ================================================

"""
You can think about a problem systematically and solve it systematically step-by-step.

You can envision different inputs, outputs, and edge cases for programs you write.

You can communicate your ideas clearly to co-workers and incorporate their suggestions.

Most importantly, you can convert your thoughts and ideas into working code that's also readable.


"""

import time

start = time.time()

for i in range(1,101):
    print(i)
    
print(time.time() - start)

#           ---------------------------------------------------- BINARY- SEARCH -----------------------------------------





#           ---------------------------------------------------- Big - O - Notation -----------------------------------------

#  BIG-O-NOTATION   --> this is used to measure how running time or space requirements for your program grows as input size grows

def get_sqr_num(numbers):
    sqr_num = []
    for n in numbers:
        sqr_num.append(n*n)
    return sqr_num

n = [2,3,5,6]
print(get_sqr_num(n))


