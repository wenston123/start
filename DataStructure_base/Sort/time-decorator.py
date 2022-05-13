import time
def func_time(func):
    def inner(*args,**kw):
        now_time = time.localtime()
        print('函数开始运行的时间为：',time.strftime('%Y:%m:%d %H:%M:%S',now_time))
        func(*args,**kw)
    return inner

@func_time
def sum(x,y):
    print(x,y)
sum(4,7)

import time

def func_time(func):
    def inner(*args,**kw):
        start_time = time.time()
        func(*args,**kw)
        end_time = time.time()
        print('函数运行时间为：',end_time-start_time,'s')
    return inner

@func_time
def sum(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(j,'*', i, '=',i*j,end='   ')
        print()
sum(9)

