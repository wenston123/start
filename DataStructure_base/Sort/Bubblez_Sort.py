'''
冒泡排序：稳定排序
时间复杂度为O(n^2)
空间复杂度为O(1)
列表每两个相邻的数，如果前面比后面大，则交换这两个数

一趟排序完成后，则无序区减少一个数，有序区增加一个数

'''

data = [3,1,6,9,2,7,0,4 ]
import random

# def Bubble(list):
#     for i in range(len(list)-1):#n-1唐，第i趟
#         for j in range(len(list)-i-1):#n-i-1未排序区域
#             if list[j]>list[j+1]:
#
#                 temp = list[j]
#                 list[j] =list[j+1]
#                 list[j+1] = temp
#         print(list)
# #
# #
# #
# #
# #
#     return list
# #
#
#
# Bubble(data)
# print(Bubble(data))
#
#
# '''
# 冒泡排序改进
# '''
# li = [9,8,7,6,5,1,2,3,4,5]
#
# def Bubble_sort(list):
#     for i in range(len(list)-1):
#
#         exchange = False
#         for j in range(len(list)-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#                 exchange = True
#         print(i)
#         if not exchange:
#
#             return list
#
# print(Bubble_sort(li))


import random
# li = list(range(30))
# random.shuffle(li)
# print(li)
# Bubble_Sort(li)
# print(li)



def Bubble_Sort(li):
    # print(li)
    for i in range(len(li)-1):##总共执行的趟数
        print(li)
        for j in range(len(li)-1-i):
            # print(li)
            if li[j]>li[j+1]:
                li[j],li[j+1] =li[j+1],li[j]
    return li
        # print(li)

def Bubble_Sort1(li):
    for i in range(len(li)-1):#执行的趟数
        # print(li)
        print(li)
        exchange = False###设置检测变量，
        for j in range(len(li)-1-i):
            if li[j] > li[j + 1]:

                li[j],li[j+1] = li[j+1],li[j]

                # print(li)
                exchange = True
        # print(li)
        if not exchange:
            return li


li = [3,4,5,0,1,2,6,7,8,9]
li1 = [3,4,5,0,1,2,6,7,8,9]
# print(li)
print(Bubble_Sort1(li))
# print(li)


print('+++++++')
print(Bubble_Sort(li1))


