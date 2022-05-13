##

def linear_search(li,val):
    for ind, v in enumerate(li):
        # print(ind)
        # print(ind,v)
        if v == val:
            return ind
    return  None


import random

li = list(range(100))
random.shuffle(li)
print(li)
##符合条件的
print(linear_search(li,20))
#
#不符合条件的
print(linear_search(li,200))
