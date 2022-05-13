
'''
双向队列：
队首队尾都能入队出队



'''
from collections import deque###双向队列
q = deque()
q.append(1)#队尾进队

print(q.popleft())#对手出队
#用于双向队列
q.appendleft(1)#队首进队
q.pop()##队尾出队


def tail(n):
    with open('test.txt','r') as f:
        q =deque(f,n)
        return q
for line in tail(5):
    print(line,end='')