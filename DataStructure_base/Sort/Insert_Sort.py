# data = [5,1,9,0,2,4,3]

#
# def insert(list):
#     for i in range(1,len(list)):
#         temp = list[i]
#         no = i-1
#         while no>=0 and temp<list[no]:#元素从后往前移动进行交换，得到第一个最小
#             list[no+1] = list[no]
#             no-=1
#         list[no+1] = temp  ##正常情况是
#     return list



# print(insert(data))

'''
插入排序：

时间复杂度为O(n^2)
最好情况为O(n)

'''
import time


# 时间装饰器
import time  #导入time模块
def cal_time(fn):  #必要的装饰器语法
    print("我是外部函数")
    def inner():  #必要的修饰器语法
        start=time.time()
        fn()
        end=time.time()
        print("代码执行耗时为{}秒".format(end - start))  #打印代码执行耗费时间
    return inner  #



import random



# 线性查找


#
# data = list(range(10000))
# # print(data)
# random.shuffle(data)
# # print(data)
# @cal_time
# def Insert_Sort():
#     data = list(range(100000))
#     # print(data)
#     random.shuffle(data)
#     for i in range(1,len(data)):#i表示摸到手里的牌的下标
#         j = i-1 #手里的牌下标
#         temp = data[i]
#         while j >= 0 and data[j] > temp:
#             data[j+1] = data[j]
#             j -= 1#继续向左检查
#         data[j+1] = temp
#     return data
# Insert_Sort()
# print(Insert_Sort(data))

##时间装饰器问题1

def Insert_Sort(li):
    for i in range(1,len(li)):##表示摸到手里的牌的下标
        j = i-1##表示手里的牌的下标
        temp = li[i] #手里的牌
        while j >= 0 and li[j] > temp:###手里的牌>摸到手里的
            li[j+1] = li[j]##现在手里的牌向后移动
            j-=1##继续向左检查
        li[j+1] = temp ##正常情况

    return li

data = list(range(10))
import random
random.shuffle(data)
print(data)

print(Insert_Sort(data))






