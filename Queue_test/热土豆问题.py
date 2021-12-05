# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/14 16:54
---------------------------------------------
"""
from Queue_test.def_Queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    # 将名字全部加入队列中
    for name in namelist:
        simqueue.enqueue(name)
    # 只剩一人时结束
    while simqueue.size() > 1:
        # 传递num次
        for i in range(num):
            # 队首出列立刻入列，在结束传递后的队首即为目标
            simqueue.enqueue(simqueue.dequeue())
        # 目标移除
        simqueue.dequeue()
    # 返回最后幸存
    return simqueue.dequeue()

print(hotPotato(namelist=['1', '2', '3', '4', '5', '6', '7'], num=7))


