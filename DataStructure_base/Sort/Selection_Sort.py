'''


快速排序，属于交换排序对一种，

一趟排序几率最小的书，放到第一个位置
再一趟排序记录，记录列表无序区的最小数，放到第二个位置

算法关键点：有序区和无序区，无序区的最小数位置
'''
import reprlib

data = [3,1,6,9,2,7,0,4 ]

#
# def Select(list):
#
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>data[j]:
#                 list[i],list[j] = list[j],list[i]
#
#
#     return list
#
# print(Select(data))

##最简单版,时间复杂度（O^3）
# def Select_Sort(list):
#     li_new =[]
#     for i in range(len(list)):
#         min_val = min(list)
#         li_new.append(min_val)
#         list.remove(min_val)
#     return li_new
# print(Select_Sort(data))


##改进版

# def Select_Sort1(list):
#     for i in range(len(list)-1):
#         min_loc =i
#         for j in range(i+1,len(list)):
#             if list[j]<list[min_loc]:
#                 min_loc = j
#         if min_loc!=i:
#
#             list[i],list[min_loc] = list[min_loc],list[i]
#         print(list)
#     return list
#
#
# li = [3,4,5,6,7,1,2]
# print(Select_Sort1(li))

# def Select_Sort(li):
#     new_list = []  ##设置一个恐列表，用来存放最小值
#     for i in range(len(li)):#遍历原始列表
#         min_val = min(li)##选择出原始列表的最小值
#         new_list.append(min_val)
#         li.remove(min_val)
#     return new_list
# li = [3,4,5,6,7,1,2]
# print(Select_Sort(li))

def Select_Sort1(li):
    for i in  range(len(li)-1):
        min_val = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_val]:
                min_val = j
        if min_val!=i:
            li[i],li[min_val] = li[min_val],li[i]
    return  li

li = [3,4,5,6,7,1,2]
print(Select_Sort1(li))


