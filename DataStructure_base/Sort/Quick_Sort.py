
import time
import random


def Quick_Sort(data,left,right):
    if left<right:##表示至少两个元素
        mid = partion(data,left,right)#第一个元素归位
        Quick_Sort(data,left,mid-1)
        Quick_Sort(data,mid+1,right)



def partion(data,left,right):
    temp =data[left]

    while left<right:
        while data[right]>= temp and left<right:#找比temp小的数
            right= right-1#向左走
        data[left] = data[right]#把右边的值写到左边
        print(li,'right')
        while data[left]<=temp and left<right:
            left+=1
        data[right] = data[left]#把左边的值写到右边
        print(li,'left')


    data[left]=temp #把temp归位
    return left
# li = [5,7,4,6,1,3,9]
# print(li)
# partion(li,0,len(li)-1)
# print(li)
# Quick_Sort(li,0, len(li)-1)
# print(li)

#快速排序的时间复杂度O(nlogn)

#快速排序的问题：
#1递归问题
#2对于有序的数组，南辕北辙最坏的时间复杂度为（n^2）

##改进型
def func_time(func):
    def inner(*args,**kw):
        start_time = time.time()
        func(*args,**kw)
        end_time = time.time()
        print('函数运行时间为：',end_time-start_time,'s')
    return inner
import random
def partion1(data,left,right):
    i = random.randint(left,right)
    # print(data[i])

    data[left] ,data[i] =data[i],data[left]



    temp =data[left]

    while left<right:
        while data[right]>= temp and left<right:#找比temp小的数
            right= right-1#向左走
        data[left] = data[right]#把右边的值写到左边
        print(li,'right')
        while data[left]<=temp and left<right:
            left+=1
        data[right] = data[left]#把左边的值写到右边
        print(li,'left')

    data[left]=temp #把temp归位
    return left
@func_time##递归调用也算做调用装饰器
def Quick_Sort1(data,left,right):
    if left<right:##表示至少两个元素
        mid = partion1(data,left,right)#第一个元素归位
        Quick_Sort1(data,left,mid-1)
        Quick_Sort1(data,mid+1,right)

# li = [5,7,4,6,1,3,9]
# print(li)
# partion1(li,0,len(li)-1)
# print(li)
li = [x for x in range(1000)]
# print(li)
random.shuffle(li)
# print(li)
Quick_Sort1(li,0, len(li)-1)
# print(li)