# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/14 16:31
---------------------------------------------
insert(i, item) --> i为位置变量，即加入到list的哪个位置；
                    item为加入的数据
append(item) --> 直接在列表尾部加入数据item
"""
class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return self.list == []

    # 复杂度O(n)
    def enqueue(self, item):
        self.list.insert(0, item)

    # 复杂度O(1)
    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)