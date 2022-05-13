#堆排序
#
'''
堆是一种特殊的完全二叉树
大根堆
小根堆




'''

#构建一个堆
#1.建立堆
#2.得到堆顶元素，为最大元素
#3.去掉堆顶，将堆最后一个元素放到对丁，此时可以通过一次调整重新使堆有序
#4.堆顶元素为第二答元素
#5.重复步骤3，直到堆变空
#
# def sift(li,low,high):
#     '''
#
#     :param li: 列表
#     :param low: 堆的根结点位置
#     :param high:堆的最后一个元素的位置，
#     :return:
#     '''
#     i = low #最开始指向根节点
#     j = 2*i+1 #j开始是左孩子
#     temp = li[low]##存储堆顶元素
#     while j <= high: #只要j位置有数
#
#         if j+1<=high and li[j+1]>li[j]:#如果右孩子比左孩子较大
#             j =j+1 #j指向右孩子，
#
#         if li[j]>temp:##
#             li[i] = li[j]###交换
#             i = j
#             j = 2*i+1#继续向下
#         else:##如果temp放入i的地方
#             li[i] =temp#把temp放入某一节领导的位置
#             break
#     else:
#         li[i] =temp##把temp放到叶子节点上
#
#
#
# def heap_sort(li):
#     n = len(li)
#     for i in range((n-2)//2,-1,-1):
#
#         #i表示建堆的时候调整的部分的根下表
#         sift(li ,i,n-1)
#     ##建堆就完成了
#     for i in (n-1,-1,-1):##当前堆的最后一个元素
#         li[0],li[i] = li[i],li[0]
#         sift(li,0,i-1)##i-1是新的high
#
#  ##时间复杂度（O^nlogn）
#
# ##堆排序的内置模块
# import heapq##q代表队列，优先队列
# import random
# li = list(range(10))
# random.shuffle(li)
# print(li)
# heap_sort(li)
# print(li)

# heapq.heapify(li)##建堆
# print(li)
# for i in range(len(li)):
#     print(heapq.heappop(li),end=',')
# # heapq.heappop(li)


#1，建立堆
#2.

def sift(li,low,high):
    '''

    :param li: 列表
    :param low: 堆的堆顶位置
    :param high: 堆的最后一个元素下标
    :return:
    '''
    i = low
    j =2*1+1#j开始是左孩子
    temp = li[low]##把对顶存起来
    while j <= high:#只要j位置有数
        if li[j+1]>li[j]:#如果右孩子比较大
            j = j+1#指向右孩子
        if




