def Count_Sort(li,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)
import random
li = [random.randint(0,100) for _ in range(1000)]
print(li)
Count_Sort(li)
print(li)

##时间复杂度O(n)
