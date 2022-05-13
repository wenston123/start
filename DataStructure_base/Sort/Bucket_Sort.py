def bucket_sort(li,n =100, max_num =10000):
    bucket =  [[] for _ in range(n)]#创建桶
    for var in li:

       i =min( var//(max_num//n),n-1) #表示i放到几号桶里
       bucket[i].append(var)
       for j in range(len(bucket[i])-1,0,-1):
           if bucket[i][j]<bucket[i][j-1]:
               bucket[i][j],bucket[i][j-1] = bucket[i][j-1],bucket[i][j]
           else:
               break
        #0-》

    sorted_li =[]
    for buc in bucket:
        sorted_li.extend(buc)
    return sorted_li
import random
li = [random.randint(0,10000)for i in range(100000)]
# print(li)
li =bucket_sort(li)
print(li)

##桶排序的时间复杂度取决于数的分布情况
#平均浮渣度O(n+k)
#最坏的时间复杂度O(n^2k)
#空间复杂度O(nk)