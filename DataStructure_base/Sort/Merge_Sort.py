##合并排序法（Merge Sort）

List1 = [20, 30, 11, 9, 0, 17]
List2 = [2, 9, 1, 0, 33, 22, 90]
'''
归并排序

# '''
#

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltemp = []
    # 假设无序
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltemp.append(li[i])
            i += 1
        else:
            ltemp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数了
    while i <= mid:
        ltemp.append(li[i])
        i = i + 1

    while j <= high:
        ltemp.append(li[j])
        j = j + 1
    li[low:high+1] = ltemp


li = [2,4,0,7,1,3,9,8]
# merge(li, 0,3,7)
# print(li)

# #
# def mergre_sort(li, low, high):
#     if low < high:  ##至少有两个元素
#         mid = (low + high) // 2
#         mergr_sort(li, low, mid)
#         mergr_sort(li, mid + 1, high)
#         merge(li, low, mid, high)

def merge_sort(li,low,high):

    if low<high:
        mid = (low + high) // 2


        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)
    # return li
# print(merge_sort(li,0,len(li)-1))
merge_sort(li,0,len(li)-1)
print(li)


li = list(range(1000))
import random
random.shuffle(li)
print(li)

merge_sort(li,0,len(li)-1)
print(li)

##时间复杂度（O(nlogn)）
#空间复杂度（O(n)）

##递归需要用到系统栈的空间。