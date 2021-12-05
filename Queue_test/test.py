# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/14 16:37
---------------------------------------------
"""
import Queue_test.def_Queue

q = Queue_test.def_Queue.Queue()

print(q.isEmpty())

q.enqueue('8')

q.enqueue('a')

q.enqueue('12')

print(q.size())

print(q.dequeue())

print(q.size())

print(q.list)