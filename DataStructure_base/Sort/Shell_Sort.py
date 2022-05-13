'''
希尔排序：

时间复杂度为O(n^3/2)

'''



def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):#表示摸到牌的下标
        temp = li[i]
        j = i -gap##手里牌的下标
        while j>=0 and li[j]>temp:
            li[j+gap] = li[j]
            j-=gap
        li[j+gap] = temp

def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        insert_sort_gap(li,d)
        d//= 2
li  = list(range(10))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)