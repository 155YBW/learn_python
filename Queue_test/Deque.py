# --- coding:utf-8 ---
"""
---------------------------------------------
__author__: 15500
___date___: 2021/11/19 10:42
---------------------------------------------
规定：列表0端做deque尾端，列表-1端作为首端
"""

class deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(-1, item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

