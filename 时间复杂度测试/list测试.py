# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/6 11:39
---------------------------------------------
"""
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("t1 cost %f s\n" % t1.timeit(number=1000))

t2 = Timer("test2()", "from __main__ import test2")
print("t2 cost %f s\n" % t2.timeit(number=1000))

t3 = Timer("test3()", "from __main__ import test3")
print("t3 cost %f s\n" % t3.timeit(number=1000))

t4 = Timer("test4()", "from __main__ import test4")
print("t4 cost %f s\n" % t4.timeit(number=1000))