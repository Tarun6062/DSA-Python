

# ====== Linear   =========    ===========================    Non-Linear    ================

# 1 - Array                                                1 -  TREES
# 2 - Linkedlist                                           2 -  Graphs
# 3 - Stacks
# 4 - Quhes
# 5 - Hashing


""" 
ARRAYS  :-  Linear DS which is used to store multiple items of same type in continuous memory location

    disadv :- 1 - fixed size  (memory wastage)
              2 - same type of data is stored    (we cannot store int, float , string in the same array)
              3 - 

"""


import ctypes

class Mylist:
    
    def __init__(self):
        self.size = 1
        self.n = 0